from django.db import models
from django.utils import timezone
# Create your models here.

class Author(models.Model):
    
    """
    Author Model
    
    """
    
    name = models.CharField(max_length = 255, required = True)
    date_of_birth = models.DateField(required = True)
    nationality = models.CharField(max_length = 255, required = True)


class Book(models.Model):
    """
    Books model
    """
    
    title = models.CharField(max_length = 255, required = True, null =False)
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null = True)
    genre = models.CharField(max_length = 255, required = True, null =False)
    publish_date = models.DateField(default=timezone.now)
    
    
