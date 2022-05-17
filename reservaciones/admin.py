from django.contrib import admin

from reservaciones import models

# Register your models here.

admin.site.register(models.Cliente)
admin.site.register(models.Habitacion)
admin.site.register(models.Reservacion)