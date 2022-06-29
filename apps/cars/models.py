from django.db import models
from django.core.validators import MaxLengthValidator, MinLengthValidator, MinValueValidator, MaxValueValidator


# Create your models here.
class CarModel(models.Model):
    class Meta:
        db_table = 'cars'

    car_name = models.CharField(max_length=20)
    car_series = models.CharField(max_length=20)
    price = models.IntegerField(validators=[
        MaxValueValidator(6000000),
        MinValueValidator(1),
    ])
    year = models.CharField(validators=[
        MaxLengthValidator(4),
        MinLengthValidator(4),
        MaxValueValidator(2022),
        MinValueValidator(1940),
    ])
    car_payload = models.CharField(max_length=20,validators=[
        MaxLengthValidator(5),
        MinLengthValidator(2),
        MaxValueValidator(10000),
        MinValueValidator(10),
    ])
