from users.models import User
from django.contrib.auth import get_user_model
from rest_auth.models import TokenModel
from rest_framework import serializers


class UserRegisterSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    dob = serializers.DateField()

def create(self, validated_data):
    password = validated_data.pop('password')
    user = User.objects.create(**validated_data)
    user.set_password(password)
    user.save()
    TokenModel.objects.create(user=user)
    return user


class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()