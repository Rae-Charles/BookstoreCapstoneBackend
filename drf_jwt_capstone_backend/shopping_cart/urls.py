from django.urls import path
from rest_framework import views
from .views import ShoppingCartList
from shopping_cart import views

urlpatterns = [
    path('', ShoppingCartList.as_view())
]