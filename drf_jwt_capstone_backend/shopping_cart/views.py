from django.shortcuts import render
from rest_framework import serializers, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes
from .models import ShoppingCart
from serializers import ShoppingCartSerializer
from django.contrib.auth.models import ShoppingCart

# Create your views here.
class ShoppingCartList(APIView):

    permission_classes = [AllowAny]

    def get(self, request):
        shopping_cart= ShoppingCart.objects.all()
        serializer = ShoppingCartSerializer(shopping_cart, many=True)
        return Response(serializer.data)