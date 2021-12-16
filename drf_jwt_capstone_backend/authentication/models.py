from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.fields import CharField

# Create your models here.

# To add new columns to the authentication_user table include the properties
# in the model below
# In order for the new columns to appear in the database run:
# 1. python manage.py makemigrations
# 2. python manage.py migrate


class User(AbstractUser):
    username = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=20) 
    email = models.CharField(max_length=50) 
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    address = models.CharField(max_length=40)
    zipcode = models.CharField(max_length=10)