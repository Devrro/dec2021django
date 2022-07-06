from django.contrib.auth import get_user_model

from rest_framework.generics import ListCreateAPIView, UpdateAPIView
from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework.response import Response
from permissions.user_permissions import IsSuperUser
from .serializer import AvatarSerializer, UserSerializer, PermissionSerializer

# Create your views here.

UserModel = get_user_model()


class UserListCreateView(ListCreateAPIView):
    serializer_class = UserSerializer
    queryset = UserModel.objects.all()
    permission_classes = (AllowAny,)


class UpdatePermissionView(UpdateAPIView):
    serializer_class = PermissionSerializer
    queryset = UserModel.objects.all()
    permission_classes = (IsSuperUser,)


        # data = self.request.data
        # user_id = kwargs.get('pk')
        # qs = self.queryset.filter(id=user_id).first()
        # print(self.get_object())
        # print(data)
        # print(user_id)
        # serializer = self.serializer_class(qs, data=data,partial=True,)
        # if serializer.is_valid(raise_exception=True):
        #     serializer.save()
        #     print(serializer.data)
        # return super().patch(request, *args, **kwargs)


class AddAvatarView(UpdateAPIView):
    serializer_class = AvatarSerializer
    permission_classes = (IsAuthenticated,)
    def get_object(self):
        return self.request.user.profile
