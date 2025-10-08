from rest_framework import generics, status, viewsets, permissions
from .models import CustomUser
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from .serializers import UserSerializer, RegisterSerializer, LoginSerializer, ProfileSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.shortcuts import get_object_or_404


# Create your views here.

# userViewset
class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    @action(detail=True, methods=['post'], permission_classes=[permissions.IsAuthenticated])
    def follow(self, request, pk=None):
        """Follow another user"""
        target_user = get_object_or_404(CustomUser, pk=pk)
        current_user = request.user

        if target_user == current_user:
            return Response({"detail": "You cannot follow yourself."}, status=status.HTTP_400_BAD_REQUEST)

        current_user.follow(target_user)
        return Response(
            {"detail": f"You are now following {target_user.username}."},
            status=status.HTTP_200_OK
        )

    @action(detail=True, methods=['post'], permission_classes=[permissions.IsAuthenticated])
    def unfollow(self, request, pk=None):
        """Unfollow a user"""
        target_user = get_object_or_404(CustomUser, pk=pk)
        current_user = request.user

        if target_user == current_user:
            return Response({"detail": "You cannot unfollow yourself."}, status=status.HTTP_400_BAD_REQUEST)

        current_user.unfollow(target_user)
        return Response(
            {"detail": f"You have unfollowed {target_user.username}."},
            status=status.HTTP_200_OK
        )
    
    @action(detail=True, methods=['get'], permission_classes=[permissions.IsAuthenticated])
    def followers(self, request, pk=None):
        """List all followers of a user"""
        user = get_object_or_404(CustomUser, pk=pk)
        followers = user.followers.all()
        serializer = UserSerializer(followers, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['get'], permission_classes=[permissions.IsAuthenticated])
    def following(self, request, pk=None):
        """List all users this user follows"""
        user = get_object_or_404(CustomUser, pk=pk)
        following = user.following.all()
        serializer = UserSerializer(following, many=True)
        return Response(serializer.data)


# register view
class RegisterAPIView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        response =  super().create(request, *args, **kwargs)
        user = CustomUser.objects.get(username=response.data['username'])
        token, _ = Token.objects.get_or_create(user = user)
        return Response({
            'user': UserSerializer(user).data,
            'token': token.key
        }, status=status.HTTP_201_CREATED)


# # login view
class LoginAPIView(generics.GenericAPIView):
    permission_classes = [AllowAny]
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = LoginSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, _ = Token.objects.get_or_create(user=user)
        return Response({
            'user': UserSerializer(user).data,
            'token': token.key
        }, status=status.HTTP_200_OK)
    
# user profile management view
class ProfileView(generics.RetrieveUpdateAPIView):
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user

    