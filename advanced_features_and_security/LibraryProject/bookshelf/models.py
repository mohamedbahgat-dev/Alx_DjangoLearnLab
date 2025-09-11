from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager, Group, Permission


# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField()

    class Meta:
    # custom permissions
        permissions = (
            ("can_view", "Can view"),
            ("can_create", "Can create"),
            ("can_edit", "Can edit"),
            ("can_delete", "Can delete")
        )
    def __str__(self):
       return self.title

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


# create groups
editors , created = Group.objects.get_or_create(name = 'Editors')
viewers , created = Group.objects.get_or_create(name = 'Viewers')
admins , created = Group.objects.get_or_create(name = 'Admins')

# get permissions 
can_view = Permission.objects.get(codename = 'can_view')
can_create = Permission.objects.get(codename = 'can_create')
can_edit = Permission.objects.get(codename = 'can_edit')
can_delete = Permission.objects.get(codename = 'can_delete')

# assign permission to groups
editors.permissions.set([can_edit,can_create])
viewers.permissions.set([can_view])
admins.permissions.set([can_create, can_delete, can_edit, can_view])
