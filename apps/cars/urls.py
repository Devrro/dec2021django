from django.urls import path
from .views import CarListCreateView,CarUpdateReadDeleteByIdView

urlpatterns = [
    path('', CarListCreateView.as_view()),
    path('/<int:pk>', CarUpdateReadDeleteByIdView.as_view()),
]