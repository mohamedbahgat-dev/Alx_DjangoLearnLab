from rest_framework import serializers
from .models import Post, Comment

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Comment
        fields = ['id', 'author', 'post', 'content', 'created_at', 'updated_at']

class PostSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many = True, read_only=True)
    class Meta:
        model = Post
        fields = ['id', 'author', 'title', 'content', 'created_at', 'updated_at']

    def validate(self, data):
        if len(data['content']) > 500:
            raise serializers.ValidationError('The content charcters are 500')
        return data
    




