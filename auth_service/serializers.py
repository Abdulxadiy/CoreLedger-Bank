from django.contrib.auth.hashers import make_password
from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('full_name', 'phone', 'email', 'password')

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User.objects.create(
            **validated_data,
            password_hash=make_password(password)
        )

        return user