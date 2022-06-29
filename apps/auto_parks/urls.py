from django.urls import path

from .views import AutoParkView
urlpatterns = [
    path('', AutoParkView.as_view())
]