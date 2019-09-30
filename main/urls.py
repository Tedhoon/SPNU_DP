from django.urls import path
from .views import *

urlpatterns = [
    path('', index , name = 'index'),
    path('menu/' , menu , name = 'menu'),
    path('bus/' , bus , name = 'bus'),
    ]
