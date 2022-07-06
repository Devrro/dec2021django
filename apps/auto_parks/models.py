from django.core.validators import RegexValidator
from django.db import models

from .enums import RegEx

# Create your models here.


class AutoParksModel(models.Model):
    class Meta:
        db_table = 'auto_parks'

    name = models.CharField(max_length=20, validators=[RegexValidator(RegEx.NAME.pattern, RegEx.NAME.msg,),])
