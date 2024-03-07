from django.db import models
from django.utils import timezone

# Create your models here.
class Author(models.Model):
    
    """
    Author Model
    """
    
    name = models.CharField(max_length = 255, null=False)
    date_of_birth = models.DateField(default=None)
    nationality = models.CharField(max_length = 255, null=False, default='Indian')
    
    def __str__(self):
        return f'{self.name}'


class Book(models.Model):
    """
    Books model
    """
    
    title = models.CharField(max_length = 255, null=False)
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null = True)
    genre = models.CharField(max_length = 255, null=False)
    publish_date = models.DateField(default=timezone.now)
    
    def __str__(self):
        return f'{self.title}'
    
    
