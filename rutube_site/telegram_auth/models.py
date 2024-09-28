from django.db import models

#from authentication.models import User

class TelegramAccount(models.Model):
    telegram_user_id = models.IntegerField()
    chat_id = models.ImageField()
    #user = models.ForeignKey(User, on_delete=models.CASCADE)

class Code(models.Model):
    telegram_user_id = models.IntegerField()
    chat_id = models.ImageField()
    code = models.TextField()
# Create your models here.
