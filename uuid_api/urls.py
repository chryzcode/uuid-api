from django.urls import path
from .views import *

urlpatterns = [
    path('', get_all_the_Models, name='get_all_the_Models'),
]