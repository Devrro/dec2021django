from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from apps.auto_parks.models import AutoParksModel

from .manager import CarManager

# Create your models here.
UserModel = get_user_model()

class CarModel(models.Model):
    class Meta:
        db_table = 'cars'
    brand = models.CharField(max_length=10)
    car_name = models.CharField(max_length=20, blank=True)
    car_series = models.CharField(max_length=20)
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE,related_name='auth_user')
    auto_parks = models.ForeignKey(AutoParksModel, on_delete=models.CASCADE, related_name='cars')

    price = models.IntegerField(validators=[
        MaxValueValidator(6000000),
        MinValueValidator(1),
    ])
    year = models.IntegerField(validators=[
        MaxValueValidator(2022),
        MinValueValidator(1940),
    ])
    car_payload = models.CharField(max_length=20,validators=[
        MaxValueValidator(10000),
        MinValueValidator(10),
    ]),

    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    used_car = models.BooleanField(default=False)
    objects = CarManager()
    def __str__(self):
        return self.car_name,self.car_series
