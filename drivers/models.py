from django.db import models

class DriverModel(models.Model):
    driver_name = models.CharField(max_length=200)
    driver_phone = models.CharField(max_length=16)
    driver_license = models.CharField(max_length=20)

    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'driverModel'
        verbose_name_plural = 'driverModel'
        
    def __str__(self):
        return self.driver_name        
