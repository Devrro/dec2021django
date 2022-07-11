from typing import Type

from django.contrib.auth import get_user_model
from django.db import transaction
from core.services.email_service import EmailService
from rest_framework.serializers import ModelSerializer, ValidationError

from .models import ProfileModel, UserModel

UserModel: Type[UserModel] = get_user_model()


class ProfileSerializer(ModelSerializer):
    class Meta:
        model = ProfileModel
        exclude = ('user',)


class AvatarSerializer(ModelSerializer):
    class Meta:
        model = ProfileModel
        fields = ('avatar',)


class PermissionSerializer(ModelSerializer):
    class Meta:
        model = UserModel
        fields = ('is_staff',)


class UserSerializer(ModelSerializer):
    profile = ProfileSerializer()

    class Meta:
        model = UserModel
        fields = (
            'id', 'email', 'password', 'is_staff', 'is_superuser', 'last_login', 'is_active', 'profile', 'created_at',
            'updated_at')
        read_only_fields = (
            'id', 'is_staff', 'is_superuser', 'is_active', 'last_login', 'profile', 'created_at', 'updated_at')

        extra_kwargs = {'password': {'write_only': True}}

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')
        if email == password and email is not None:
            raise ValidationError(f'email cant be equal to password')
        return super().validate(attrs)

    def validate_profile(self, value):
        name = value['name']
        if name.lower() == 'felix':
            raise ValidationError('Name can`t be felix')

    @transaction.atomic
    def create(self, validated_data: dict):
        print(validated_data)
        profile = validated_data.pop('profile')
        user = UserModel.objects.create_user(**validated_data)
        ProfileModel.objects.create(**profile, user=user)

        EmailService.register_email(user)
        return user

