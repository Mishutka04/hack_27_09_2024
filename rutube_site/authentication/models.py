from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    username = models.CharField(max_length=50, verbose_name="Никнейм", unique=True)
    password = models.CharField(max_length=50, verbose_name="Пароль")
# Create your models here.
