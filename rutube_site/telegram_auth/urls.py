from django.urls import path
from telegram_auth import views

app_name = 'telegram_auth'

urlpatterns = [
    path("tg_auth/", views.AuthTelegramAPIView.as_view()),
]