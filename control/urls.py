from django.urls import path, re_path
from .views import ControlView,Create

urlpatterns = [
    re_path(r'^controlitens/(?:(?P<pk>\d+)/)?(?:(?P<action>\w+)/)?', ControlView.as_view(),
            name='controlitens'),
    path("create_control",Create.as_view(),name="create_control")
]