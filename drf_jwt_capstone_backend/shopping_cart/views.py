from django.shortcuts import render
from rest_framework import serializers, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes
from .models import ShoppingCart
from .serializers import ShoppingCartSerializer, BooksSerializer
from django.apps import apps
# Create your views here.

class ShoppingCartList(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request, Id):
        # need to filter on front end
        # users_shopping_cart_items = ShoppingCart.objects.filter(user_id=request.user.id)
        Books = apps.get_model('books.Books')
        users_books = Books.objects.filter(shoppingcart__user=Id)
        serializer = BooksSerializer(users_books, many=True)
        return Response(serializer.data)


    def post(self, request):

        if request.method == 'POST':
            serializer = ShoppingCartSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save(user=request.user)
                return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, pk):
        books = self.get_books(pk)
        books.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)   



    # users_shopping_cart_items = Book.objects.filter
    # serializer = ShoppingCartSerializer(shopping_cart, many=True)
    # # return Response(serializer.data)
    # if request.method == 'GET':
    #     books = Books.objects.filter(user_id=request.user.id)
    #     books=apps.get_model('books.Books')
    #     serializer = ShoppingCartSerializer(books, many=True)
    #     return Response(serializer.data)