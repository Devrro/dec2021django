from django.db import models


# Create your models here.


class ComputerModel(models.Model):
    class Meta:
        db_table = 'pc_model'

    brand = models.CharField(max_length=20)
    model = models.CharField(max_length=20)
    ram = models.IntegerField()
    tv = models.IntegerField()
