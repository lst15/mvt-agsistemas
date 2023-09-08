# -*- encoding: utf-8 -*-
"""

"""

from django.contrib import admin

from vehicles.models import VehicleModel
from import_export import resources
from import_export.admin import ImportMixin


class TransactionResource(resources.ModelResource):
    class Meta:
        model = VehicleModel
        #fields = ['id', 'bill_for', 'issue_date', 'due_date', 'total', 'status', 'created_time']
        fields = ['id','vehicle_plate','vehicle_brand','vehicle_model','vehicle_oil_change_km']


@admin.register(VehicleModel)
class TransactionAdmin(ImportMixin, admin.ModelAdmin):
    list_display =  ['id','vehicle_plate','vehicle_brand','vehicle_model','vehicle_oil_change_km']
    resource_class = TransactionResource
