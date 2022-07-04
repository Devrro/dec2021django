from django.shortcuts import render

from rest_framework.generics import CreateAPIView, ListCreateAPIView, RetrieveDestroyAPIView
# Create your views here.
from rest_framework.permissions import IsAuthenticated

from .models import AutoParksModel
from .serializers import AutoParkSerializer


class AutoParkView(ListCreateAPIView):
    serializer_class = AutoParkSerializer
    queryset = AutoParksModel.objects.all()


class AutoParkRetrieveDestroy(RetrieveDestroyAPIView):
    serializer_class = AutoParkSerializer
    queryset = AutoParksModel


class AutoParkCreateView(CreateAPIView):
    serializer_class = AutoParkSerializer
    queryset = AutoParksModel
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        auto_park = self.get_object()
        serializer.save(auto_park=auto_park)
        super().perform_create(serializer)
