from django.db import models
from django.contrib.auth import get_user_model
from django.http.response import Http404
from rest_framework.views import APIView
User = get_user_model()

# Create your models here.
class Books(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    author= models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    price = models.DecimalField(default=0, decimal_places=2, max_digits=5)