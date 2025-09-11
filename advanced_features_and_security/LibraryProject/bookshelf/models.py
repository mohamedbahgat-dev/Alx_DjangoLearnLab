from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import BaseUserManager

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField()

# user manager for custom user
class CustomUserManager(BaseUserManager):
    def create_user(self, email, name, password , **kwargs):
        email = self.normalize_email(email)
        user = self.model(email, name, **kwargs)
        user.set_password(password)
        user.save()
        return user 
    def create_superuser(self, email, name, password, **kwargs):
        kwargs.setdefault('is_superuser', True)
        return self.create_user(email, name, password, kwargs)


# custom user model
class CustomUser(AbstractUser):
    date_of_birth = models.DateField()
    profile_photo = models.ImageField(upload_to='book_images/')
    objects = CustomUserManager()

