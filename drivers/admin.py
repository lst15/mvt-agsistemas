# -*- encoding: utf-8 -*-
"""

"""

from django.contrib import admin

from drivers.models import DriverModel
from import_export import resources
from import_export.admin import ImportMixin

class TransactionResource(resources.ModelResource):
    class Meta:
        model = DriverModel
        #fields = ['id', 'bill_for', 'issue_date', 'due_date', 'total', 'status', 'created_time']
        fields = ['id','driver_name','driver_phone','driver_license']


@admin.register(DriverModel)
class TransactionAdmin(ImportMixin, admin.ModelAdmin):
    list_display = ['id','driver_name','driver_phone','driver_license']
    resource_class = TransactionResource
