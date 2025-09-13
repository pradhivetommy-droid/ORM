from django.db import models
from django.contrib import admin

class car_DB(models.Model):
    car_company = models.CharField(max_length=20)
    car_modelno = models.IntegerField(primary_key=True)
    car_version = models.FloatField()
    car_color = models.CharField(max_length=15)
    car_type = models.CharField(max_length=15)

class car_DBAdmin(admin.ModelAdmin):
    list_display = ["car_company", "car_modelno", "car_version", "car_color", "car_type"]
