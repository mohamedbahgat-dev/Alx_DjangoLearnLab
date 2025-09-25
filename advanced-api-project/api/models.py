from django.db import models

# Create your models here.

# Author model with name of author field
class Author(models.Model):
    name = models.CharField(max_length=100)

# Book model with 3 fields (book title, publication_year and author name which is a foreign key (one to many relashionship) for author model)
class Book(models.Model):
    title = models.CharField(max_length=200)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author,on_delete=models.CASCADE)

    def __str__(self):
        return self.title


