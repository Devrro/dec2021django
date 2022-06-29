from rest_framework.serializers import ModelSerializer


class CarSerializer(ModelSerializer):

    fields = ('id','car_name','car_series','price','year','car_payload')
