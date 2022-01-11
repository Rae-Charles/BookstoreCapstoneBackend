from django.urls import path
from rest_framework import views
from .views import ShoppingCartList

urlpatterns = [
    path('<int:Id>', ShoppingCartList.as_view())
]