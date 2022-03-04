from django.urls import path
from AppViajes.views import *
app_name = 'AppViajes' 

#AppViajes='accounts'

urlpatterns = [
    path('inicio/',inicio ,name="Inicio"),
    path('pages/',pages ,name="Pages"),
    path('<str:slug>/', detallepost,name="Detalle_post"),

]
