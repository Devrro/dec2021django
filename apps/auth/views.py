from django.contrib.auth import get_user_model

from rest_framework import status
from rest_framework.generics import GenericAPIView, get_object_or_404
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from core.services.email_service import EmailService
from core.services.jwt_service import JwtService

from apps.users.serializer import UserSerializer

from .serializers import EmailSerializer, UserPasswordSerializer

UserModel = get_user_model()


class ActivateUserView(GenericAPIView):
    permission_classes = (AllowAny,)

    def get(self, *args, **kwargs):
        token = kwargs.get('token')
        user = JwtService.validate_token(token)
        user.is_active = True
        user.save()
        return Response(status=status.HTTP_200_OK)


class ResetUserPasswordView(GenericAPIView):
    permission_classes = (AllowAny,)

    def post(self, *args, **kwargs):
        email = self.request.data.get('email')
        serializer = EmailSerializer(data={'email': email}, partial=True)
        if serializer.is_valid(raise_exception=True):
            user = get_object_or_404(UserModel, email=email)
            EmailService.reset_password(user)

        return Response('Reset password was sent. Check your email', status=status.HTTP_200_OK)


class ConfirmResettingPassword(GenericAPIView):
    permission_classes = (AllowAny,)

    def post(self, *args, **kwargs):
        token = kwargs.get('token')
        user = JwtService.validate_reset_token(token)
        password = self.request.data.get("password")
        serializer = UserPasswordSerializer(data={'password': password} )
        if serializer.is_valid(raise_exception=True):
            user.set_password(password)
            user.save()
        return Response('Password was changed!', status=status.HTTP_200_OK)
