from django.contrib.auth import get_user_model
# from books.views import get_all_books
from django.apps import apps
from .serializers import RegistrationSerializer
from books.serializers import BooksSerializer 
# from shopping_Cart.serializers import ShoppingCartSerializer
from rest_framework import generics
from rest_framework.permissions import AllowAny
User = get_user_model()
Books = apps.get_model('books.Books')


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegistrationSerializer

class BooksView(generics.CreateAPIView):
    queryset = Books.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = BooksSerializer

# class ShoppingCartView(generics.CreateAPIView):
#     queryset = ShoppingCart.objects.all()
#     permission_classes = (AllowAny,)
#     serializer_class = ShoppingCartSerializer    
