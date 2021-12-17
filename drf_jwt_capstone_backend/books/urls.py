from django.urls import path
from books import views

urlpatterns = [
    path('', views.BooksList.as_view())
]