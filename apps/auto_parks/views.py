from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, CreateAPIView, RetrieveDestroyAPIView
# Create your views here.
from .serializers import AutoParkSerializer
from .models import AutoParksModel


class AutoParkView(ListCreateAPIView):
    serializer_class = AutoParkSerializer
    queryset = AutoParksModel.objects.all()

class AutoParkRetrieveDestroy(RetrieveDestroyAPIView):
    serializer_class = AutoParkSerializer
    queryset = AutoParksModel

class AutoParkCreateView(CreateAPIView):
    serializer_class = AutoParkSerializer
    queryset = AutoParksModel

    def perform_create(self, serializer):
        auto_park = self.get_object()
        serializer.save(auto_park=auto_park)
        super().perform_create(serializer)
