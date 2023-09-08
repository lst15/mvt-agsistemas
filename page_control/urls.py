from django.urls import path, re_path
from .views import index,pages

urlpatterns = [
  path('', index, name='home'),  
  re_path(r'^.*\.*', pages, name='pages'),
]