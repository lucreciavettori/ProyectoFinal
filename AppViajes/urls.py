from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LogoutView
from AppViajes.views import *
from AppAccounts.views import *
   

app_name = 'AppViajes' 

urlpatterns = [
    path('',inicio ,name="Inicio"),
    path('pages/',pages ,name="Pages"),
    path('about/',about,name="About"),
    path('mensajes/',detallemensajes.as_view() ,name="Mensajes"),
    path('<str:slug>/', detallepost,name="Detalle_post"),
    path('account/login/', login_request,name="Login"),
    path('account/logout/', LogoutView.as_view(template_name='AppAccounts/logout.html'),name="Logout"),
    path('listar_post',ListarPost.as_view(), name='listar_post'),
    path('crear_post',CrearPost.as_view(),name="Crear_post"),
    path('editar_post/<int:pk>',EditarPost.as_view(),name="Editar_post"),
    path('eliminar_post/<int:pk>',EliminarPost.as_view(),name="Eliminar_post"),
    path('account/signup/', register,name="Register"),
    path('account/profile/', profile,name="profile"),
    path('account/profile_view/',profile_view,name="profile_view"),
]
