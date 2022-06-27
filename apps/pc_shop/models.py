from django.db import models


# Create your models here.
class PcModel(models.Model):
    class Meta:
        db_table = 'pc_shop'
        verbose_name = 'PC'
        verbose_name_plural = 'PC`s'
    brand = models.CharField(max_length=20)
    model = models.CharField(max_length=20)
    ram = models.IntegerField()
    tv_size = models.IntegerField()

    def __str__(self):
        return self.model
