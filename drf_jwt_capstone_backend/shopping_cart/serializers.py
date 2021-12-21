from rest_framework import serializers
from .models import ShoppingCart

class ShoppingCartSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShoppingCart
        fields = ['id', 'user_id', 'book_id', 'quantity']
