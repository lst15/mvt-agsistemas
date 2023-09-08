from django.urls import path, re_path
from .views import VehicleView,CreateX

urlpatterns = [
    re_path(r'^vehicleitens/(?:(?P<pk>\d+)/)?(?:(?P<action>\w+)/)?', VehicleView.as_view(),
            name='vehicleitens'),

    path("create_vehicle",CreateX.as_view(),name="create_vehicle")
]