from django.db import models
from drivers.models import DriverModel
from vehicles.models import VehicleModel

class ControlModel(models.Model):
    vehicle = models.ForeignKey(VehicleModel, on_delete=models.CASCADE)
    driver = models.ForeignKey(DriverModel, on_delete=models.CASCADE)
    departure_date = models.DateField()
    departure_time = models.TimeField()
    departure_km = models.PositiveIntegerField()
    departure_destination = models.CharField(max_length=200)
    return_date = models.DateField(null=True, blank=True)
    return_time = models.TimeField(null=True, blank=True)
    return_km = models.PositiveIntegerField(null=True, blank=True)
    distance_traveled = models.PositiveIntegerField(null=True, blank=True)
    
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)    
    
    class Meta:
      ordering = ['-departure_date']
      db_table = 'control'
      verbose_name = 'controlModel'
      verbose_name_plural = 'controlModel'
      
    def save(self, *args, **kwargs):
      if self.return_km:
          self.distance_traveled = int(self.return_km) - int(self.departure_km)

      super(ControlModel, self).save(*args, **kwargs)  