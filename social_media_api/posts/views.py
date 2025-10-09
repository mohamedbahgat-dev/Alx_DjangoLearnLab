from django.shortcuts import render
from rest_framework import viewsets, permissions, filters, status
from .models import Post, Comment, Like
from notifications.models import Notification
from .serializers import PostSerializer, CommentSerializer
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from django.shortcuts import get_object_or_404
from rest_framework.response import Response




# Create your views here.
class IsAuthorOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author == request.user
    
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]

    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['author']  # optional: filter by author id
    search_fields = ['title', 'content']  # 👈 allows searching by title or content
    ordering_fields = ['published_date', 'title']  # optional ordering fields

    def perform_create(self, serializer):
       serializer.save(author = self.request.user)

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]

    def perform_create(self, serializer):
       serializer.save(author = self.request.user)


class FeedView(generics.ListAPIView):
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        following_users = user.following.all()
        return Post.objects.filter(author__in=following_users).order_by('-published_date')
    

class LikePostView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        user = request.user

        # Check if user already liked this post
        if Like.objects.filter(user=user, post=post).exists():
            return Response({'detail': 'You already liked this post.'}, status=status.HTTP_400_BAD_REQUEST)

        Like.objects.create(user=user, post=post)

        # Create a notification for the post author
        if post.author != user:
            Notification.objects.create(
                recipient=post.author,
                actor=user,
                verb='liked your post',
                target=post,
            )

        return Response({'detail': 'Post liked successfully.'}, status=status.HTTP_201_CREATED)


class UnlikePostView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        user = request.user

        like = Like.objects.filter(user=user, post=post).first()
        if not like:
            return Response({'detail': 'You have not liked this post.'}, status=status.HTTP_400_BAD_REQUEST)

        like.delete()
        return Response({'detail': 'Post unliked successfully.'}, status=status.HTTP_200_OK)
