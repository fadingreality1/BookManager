from rest_framework import serializers
from .models import *

class AuthorSerializer(serializers.ModelSerializer):
    
    id = serializers.IntegerField(read_only=True)
    
    class Meta:
        model = Author
        fields = ['id', 'name', 'date_of_birth', 'nationality']
        


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'


class BookSerializerGet(serializers.ModelSerializer):
    
    id = serializers.IntegerField(read_only=True)
    author = serializers.SerializerMethodField()
    
    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'publish_date', 'genre']

    def get_author(self, obj:Author):
        return f'{obj.author.name}'
        
        

        