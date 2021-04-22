from django.db import models

# Create your models here.


class Author(models.Model):
    first = models.CharField(max_length=32)
    second = models.CharField(max_length=32)

    def __str__(self):
        return f"{self.first} {self.second}"

class Book(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=100)
    author = models.ManyToManyField(Author, blank=True, related_name="author")
    isbn = models.CharField(max_length=13)
    
    def __str__(self):
        return self.title
