from rest_framework.serializers import ModelSerializer
from .models import PcModel


class PcSerializer(ModelSerializer):
    class Meta:
        model = PcModel
        fields = ('brand', 'model', 'ram', 'tv_size')
        # fields = '__all__'
