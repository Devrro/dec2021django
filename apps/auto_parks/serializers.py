from rest_framework.serializers import ModelSerializer
from .models import AutoParksModel
from apps.cars.serializer import CarSerializer


class AutoParkSerializer(ModelSerializer):

    cars = CarSerializer(many=True, read_only=True)

    class Meta:
        model = AutoParksModel
        fields = ('id', 'name', 'cars')
