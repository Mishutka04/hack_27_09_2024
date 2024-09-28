from django.contrib import admin
from .models import QueryAnswer  # Импортируем модель

# Регистрируем модель в админке
admin.site.register(QueryAnswer)
