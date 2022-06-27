from django.contrib import admin
from .models import PcModel


# Register your models here.

@admin.register(PcModel)
class PcAdmin(admin.ModelAdmin):
    list_display = ('id', 'brand', 'model', 'ram', 'tv_size')


# admin.site.register(PcModel)
