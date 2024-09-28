from django.urls import path
from authentication import views

app_name = 'authentication'

urlpatterns = [
     path('auth/reg/', views.RegistrationAPIView.as_view(), name='auth_email'),
     path('auth/log/', views.LoginView.as_view(), name='auth_email'),
]