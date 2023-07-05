from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.TextField(max_length=250)
    subtitle = models.TextField(max_length=250)
    author = models.TextField(max_length=100)
    isbn = models.TextField(max_length=13)
    
    def __str__(self):
        return self.title