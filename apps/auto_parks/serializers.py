from rest_framework.serializers import ModelSerializer
from .models import AutoParksModel


class AutoParkSerializer(ModelSerializer):
    class Meta:
        model = AutoParksModel
        fields = ('id','name')
