from rest_framework import generics, status, permissions
from .models import Book, Author
from .serializers import BookSerializer, AuthorSerializer
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response


# Create your views here.
class ListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class CreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer()
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        title = self.request.data.get('title')
        if not title or len(title.strip()) < 3:
            raise ValidationError({"title": "Title must be at least 3 characters long."})
        serializer.save()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data = request.data)
        serializer.is_valid(raise_exception=True)
    
        self.perform_create(serializer)
        return Response(
            {
                "message": "Book created successfully",
                "book": serializer.data
            },
            status=status.HTTP_201_CREATED
        )


class DetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer()
    permission_classes = [permissions.AllowAny]

class UpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer()
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        title = self.request.data.get('title')
        if not title or len(title.strip()) < 3:
            raise ValidationError({"title": "Title must be at least 3 characters long."})
        serializer.save()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data = request.data)
        serializer.is_valid(raise_exception=True)
    
        self.perform_create(serializer)
        return Response(
            {
                "message": "Book updated successfully",
                "book": serializer.data
            },
            status=status.HTTP_200_OK
        )

class DeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer()
    permission_classes = [permissions.IsAuthenticated]
