from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes
from .models import Books
from .serializers import BooksSerializer
from django.contrib.auth.models import User

# Create your views here.
@api_view(['GET'])
@permission_classes([AllowAny])
def get_all_books(request):
    books = Books.objects.all()
    serializer = BooksSerializer(books, many=True)
    return Response(serializer.data)