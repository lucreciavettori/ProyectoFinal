from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LogoutView
from AppViajes.views import *
from AppAccounts.views import login_request, register

app_name = 'AppViajes' 

#AppViajes='accounts'

urlpatterns = [
    path('inicio/',inicio ,name="Inicio"),
    path('pages/',pages ,name="Pages"),
    path('mensajes/',detallemensajes ,name="Mensajes"),
    path('<str:slug>/', detallepost,name="Detalle_post"),
    path('account/login/', login_request,name="Login"),
    path('account/logout/', LogoutView.as_view(template_name='AppAccounts/logout.html'),name="Logout"),
    path('account/register/', register,name="Register"),

]
