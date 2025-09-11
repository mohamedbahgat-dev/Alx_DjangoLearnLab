from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import BaseUserManager

# Create your models here.

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




class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=400)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')

    class Meta:
        # custom permissions
        permissions = (
            ("can_add_book", "Can add book"),
            ("can_change_book", "Can change book"),
            ("can_delete_book", "Can delete book"),
        )
    def __str__(self):
        return self.title

class Library(models.Model):
    name = models.CharField(max_length=100)
    books = models.ManyToManyField(Book, related_name='library')

    def __str__(self):
        return f"The library name is: {self.name}"

class Librarian(models.Model):
    name = models.CharField(max_length=100)
    library = models.OneToOneField(Library, on_delete=models.CASCADE, related_name='librarian')

    def __str__(self):
        return self.name

class UserProfile(models.Model):
    class Role(models.TextChoices):
        
        ADMIN = 'ADMIN', 'Admin'
        STAFF = 'STAFF', 'Staff'
        MEMBER = 'MEMBER', 'Member'

    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='profile')
    role = models.CharField(max_length=50, choices=Role.choices, default=Role.MEMBER)

    def __str__(self):
        return f"{self.user.username}'s Profile ({self.role})"
    

# django signal func
@receiver(post_save, sender = CustomUser)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user = instance)
        instance.profile.save()

