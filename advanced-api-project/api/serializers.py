from rest_framework import serializers
from .models import Book, Author
from datetime import datetime

# serializer model for book model that serialize all book fields with validation of publication year to ensure that publication year not in the future 
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

    def validate(self, data):
        if data['publication_year'] > datetime.now().year:
            raise serializers.ValidationError("Publication year can not be in the future")

# model that serialize the author model fields with extended nested object that dynamically get all books that written by this author
class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(read_only=True, many=True)
    class Meta:
        model = Author
        fields = 'name'