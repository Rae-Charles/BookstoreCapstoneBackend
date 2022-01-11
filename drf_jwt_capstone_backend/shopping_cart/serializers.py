from rest_framework import serializers
from .models import ShoppingCart
from django.apps import apps

Books = apps.get_model('books.Books')

class ShoppingCartSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShoppingCart
        fields = ['id', 'user_id', 'book', 'quantity']

class BooksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = ['id', 'title', 'author', 'genre', 'description', 'price']