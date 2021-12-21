from django.shortcuts import render
from rest_framework import serializers, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes
from .models import ShoppingCart
from .serializers import ShoppingCartSerializer


# Create your views here.
class ShoppingCartList(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):
        # need to filter on front end
        shopping_cart= ShoppingCart.objects.all()
        serializer = ShoppingCartSerializer(shopping_cart, many=True)
        return Response(serializer.data)


    def post(self, request):

        if request.method == 'POST':
            serializer = ShoppingCartSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save(user=request.user)
                return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  


    def delete(self, request, pk):
        books = ShoppingCart.get_books(pk)
        books.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)      


