from django.urls import path
from AppViajes.views import *

urlpatterns = [
    path('inicio/', inicio,name="Inicio"),
]
