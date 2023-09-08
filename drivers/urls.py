from django.urls import path, re_path
from .views import DriverView,Create

urlpatterns = [
    re_path(r'^driveritens/(?:(?P<pk>\d+)/)?(?:(?P<action>\w+)/)?', DriverView.as_view(),
            name='driveritens'),
    
    path("create_driver",Create.as_view(),name="create_driver")
]