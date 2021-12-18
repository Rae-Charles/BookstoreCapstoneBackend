from django.urls import path
from books import views

urlpatterns = [
    path('allbooks/', views.get_all_books)
]