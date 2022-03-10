from django.contrib import admin
from AppViajes.models import *

# Registramos los modelos

class PostAdmin(admin.ModelAdmin):
    search_fields= ['autor']
    list_display= ('titulo','autor','fecha_creacion')

class MensajeAdmin(admin.ModelAdmin):
    search_fields= ['autor_mensaje']
    list_display= ('dirigido_a','autor_mensaje','fecha_creacion_mensaje')


admin.site.register(Post, PostAdmin)
admin.site.register(Mensaje, MensajeAdmin)