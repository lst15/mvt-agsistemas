# -*- encoding: utf-8 -*-
"""

"""

from django.contrib import admin

from control.models import ControlModel
from import_export import resources
from import_export.admin import ImportMixin


class TransactionResource(resources.ModelResource):
    class Meta:
        model = ControlModel
        # fields = ['id', 'bill_for', 'issue_date', 'due_date', 'total', 'status', 'created_time']
        fields = [
            'id'
            'vehicle',
            'driver',
            'departure_date',
            'departure_time',
            'departure_km',
            'departure_destination',
            'return_date',
            'return_time',
            'return_km',
            'distance_traveled'
        ]


@admin.register(ControlModel)
class TransactionAdmin(ImportMixin, admin.ModelAdmin):
    list_display = [
        'id',
        'vehicle',
        'driver',
        'departure_date',
        'departure_time',
        'departure_km',
        'departure_destination',
        'return_date',
        'return_time',
        'return_km',
        'distance_traveled'
    ]
    resource_class = TransactionResource
