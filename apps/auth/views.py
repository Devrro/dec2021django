from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from core.services.jwt_service import JwtService
from django.contrib.auth import get_user_model
from core.services.email_service import EmailService
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
        data = self.request.data.get('email')
        try:
            user = UserModel.objects.get(email=data)
        except:
            return Response('User not found', status=status.HTTP_400_BAD_REQUEST)

        if user:
            EmailService.reset_password(user)
            return Response('Reset password was sent. Check your email', status=status.HTTP_200_OK)


class ConfirmResettingPassword(GenericAPIView):
    permission_classes = (AllowAny,)
    def post(self,*args, **kwargs):

        token = kwargs.get('token')
        user = JwtService.validate_reset_token(token)
        data = self.request.data.get("password")
        user.set_password(data)
        user.save()
        return Response(status=status.HTTP_200_OK)
