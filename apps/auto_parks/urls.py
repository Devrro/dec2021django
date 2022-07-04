from django.urls import path

from .views import AutoParkCreateView, AutoParkRetrieveDestroy, AutoParkView

urlpatterns = [
    path('', AutoParkView.as_view()),
    path('/<int:pk>', AutoParkRetrieveDestroy.as_view()),
    path('/<int:pk>/cars', AutoParkCreateView.as_view()),
]