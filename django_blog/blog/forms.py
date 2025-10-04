from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm, ValidationError
from .models import Post, Comment

from django import forms

class CustomeCreationFrom(UserCreationForm):
    class Meta:
        model = User
        fields = ('username','email',)

class ProfileForm(ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']

    def clean_title(self):
        title = self.cleaned_data.get('title')
        if len(title) < 5 : 
            raise ValidationError('The title must be at least 5 characters long')
        return title
        
    def clean_content(self):
        content = self.cleaned_data.get('content')
        if len(content) > 500 : 
                raise ValidationError('The content must be 500 char max')
        return content
    

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']

    def clean_content(self):
        content = self.cleaned_data.get('content')
        if content.strip() == '' or not content:
            raise ValidationError('Comment can not be empty.')
        
        if len(content) < 3 : 
            raise ValidationError('Comment must be at least 3 characters')
    
        return content

