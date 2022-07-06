from django.contrib.auth import get_user_model

from rest_framework.generics import ListCreateAPIView, UpdateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from permissions.user_permissions import IsSuperUser
from .serializer import AvatarSerializer, UserSerializer,PermissionSerializer
# Create your views here.

UserModel = get_user_model()


class UserListCreateView(ListCreateAPIView):
    serializer_class = UserSerializer
    queryset = UserModel.objects.all()
    permission_classes = (AllowAny,)


class UpdatePermissionView(UpdateAPIView):
    serializer_class = UserSerializer
    queryset = UserModel.objects.all()
    permission_classes = (IsSuperUser,)

    def patch(self, request, *args, **kwargs):

        instance = self.get_object()
        data = self.request.data
        serializer = self.serializer_class(instance, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return super().patch(request, *args, **kwargs)
            # return Response(serializer.data)
        else:
            return Response("Can`t update user permission")



class AddAvatarView(UpdateAPIView):
    serializer_class = AvatarSerializer

    def get_object(self):
        return self.request.user.profile
