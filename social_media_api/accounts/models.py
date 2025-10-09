from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    bio = models.TextField()
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    following = models.ManyToManyField(
        'self',
        symmetrical=False,
        related_name='followers',
        blank=True
    )

    def follow(self, user):
        """Follow another user."""
        self.following.add(user)

    def unfollow(self, user):
        """Unfollow a user."""
        self.following.remove(user)

    def is_following(self, user):
        """Check if the current user is following another user."""
        return self.following.filter(id=user.id).exists()

    def is_followed_by(self, user):
        """Check if another user follows the current user."""
        return self.followers.filter(id=user.id).exists()

    def __str__(self):
        return self.username