from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=400)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')

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

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    role = models.CharField(max_length=50, choices=Role.choices, default=Role.MEMBER)

    def __str__(self):
        return f"{self.user.username}'s Profile ({self.role})"
    

# django signal func
@receiver(post_save, sender = User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user = instance)
        instance.profile.save()

