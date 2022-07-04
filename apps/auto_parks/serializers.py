from rest_framework.serializers import ModelSerializer

from apps.cars.serializer import CarSerializer

from .models import AutoParksModel


class AutoParkSerializer(ModelSerializer):

    cars = CarSerializer(many=True, read_only=True)

    class Meta:
        model = AutoParksModel
        fields = ('id', 'name', 'cars')
