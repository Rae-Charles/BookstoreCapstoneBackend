from django.urls import path
from books import views
from .views import BooksDetail

urlpatterns = [
    path('', views.get_all_books),
    path('api/books/<int:pk>', views.BooksDetail.as_view()),
]