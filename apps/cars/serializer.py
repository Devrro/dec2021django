from rest_framework.serializers import ModelSerializer
from .models import CarModel


class CarSerializer(ModelSerializer):
    class Meta:
        model = CarModel
        fields = ('id', 'brand', 'car_name', 'car_series', 'price', 'year', 'created_at', 'updated_at')
