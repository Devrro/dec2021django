from django.urls import path

from .views import AddAvatarView, UpdatePermissionView, UserListCreateView

urlpatterns = [
    path('', UserListCreateView.as_view()),
    path('/permissions/<int:pk>', UpdatePermissionView.as_view()),
    path('/avatars', AddAvatarView.as_view()),

]