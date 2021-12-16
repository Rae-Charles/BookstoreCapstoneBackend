from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your models here.
class Books(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    author= models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    price = models.IntegerField
    