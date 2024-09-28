from rest_framework import serializers
from django.contrib.auth import get_user_model, authenticate

from .models import User


class UserRegisterSerializer(serializers.ModelSerializer):
    username = serializers.CharField()

    class Meta:
        model = User
        fields = ["username", "password"]


    def validate_username(self, username):
        """
        Check that the start is before the stop.
        """
        if User.objects.filter(username=username):
            raise serializers.ValidationError("finish must occur after start")
        return username
