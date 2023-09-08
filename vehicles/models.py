# -*- encoding: utf-8 -*-
"""

"""

from django.db import models

class VehicleModel(models.Model):
    vehicle_plate = models.CharField(max_length=10)
    vehicle_brand = models.CharField(max_length=100)
    vehicle_model = models.CharField(max_length=100,default="ae")
    vehicle_oil_change_km = models.IntegerField(default=0)

    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'vehicleModel'
        verbose_name_plural = 'vehicleModel'