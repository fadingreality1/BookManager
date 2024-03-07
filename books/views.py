from django.shortcuts import render
from rest_framework.mixins import *
from rest_framework.viewsets import ModelViewSet
from .models import *
from .serializers import *


class AuthorViewSet(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    
    
    
class BookViewSet(ModelViewSet):
    queryset = Book.objects.select_related('author').all()
    
    def get_serializer_class(self):
        if self.request.method == 'GET':
            return BookSerializerGet
        return BookSerializer
    
