from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes
from .models import Books
from .serializers import BooksSerializer
from django.contrib.auth.models import User
from django.http import Http404


# Create your views here.
@api_view(['GET'])
@permission_classes([AllowAny])
def get_all_books(request):
    books = Books.objects.all()
    serializer = BooksSerializer(books, many=True)
    return Response(serializer.data)



class BooksDetail(APIView):

    def get_books(self, pk):
        try:
            return Books.objects.get(pk=pk)
        except Books.DoesNotExist:
            raise Http404


    def get(self, request, pk):
        Books=self.get_books(pk)
        serializer = BooksSerializer(Books)
        return Response(serializer.data)                