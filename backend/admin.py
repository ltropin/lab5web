from django.contrib import admin
from backend import models

admin.site.register(models.Route)
admin.site.register(models.Driver)
admin.site.register(models.Vehicle)
admin.site.register(models.Station)
