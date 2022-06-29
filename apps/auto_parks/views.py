from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView
# Create your views here.
from .serializers import AutoParkSerializer
from .models import AutoParksModel


class AutoParkView(ListCreateAPIView):
    serializer_class = AutoParkSerializer
    queryset = AutoParksModel.objects.all()


class AutoParkUpdateRetrieveDestroyView(ListCreateAPIView):
    serializer_class = AutoParkSerializer
    queryset = AutoParksModel.objects.all()
