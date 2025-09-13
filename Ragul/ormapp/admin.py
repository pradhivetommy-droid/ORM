from django.contrib import admin
from .models import car_DB, car_DBAdmin
admin.site.register(car_DB, car_DBAdmin)
