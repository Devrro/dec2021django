from django.db import models
from django.core.validators import MaxLengthValidator, MinLengthValidator, MinValueValidator, MaxValueValidator
from apps.auto_parks.models import AutoParksModel

# Create your models here.


class CarModel(models.Model):
    class Meta:
        db_table = 'cars'
    brand = models.CharField(max_length=10)
    car_name = models.CharField(max_length=20)
    car_series = models.CharField(max_length=20)

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

    def __str__(self):
        return self.car_name,self.car_series
