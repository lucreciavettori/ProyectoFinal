from django.contrib import admin
from AppViajes.models import *

# Registramos los modelos

class PostAdmin(admin.ModelAdmin):
    search_fields= ['titulo']
    list_display= ('titulo','autor','fecha_creacion')
    

class MensajeAdmin(admin.ModelAdmin):
    list_display= ('dirigido_a','autor_mensaje','fecha_creacion_mensaje')


admin.site.register(Post, PostAdmin)
admin.site.register(Mensaje, MensajeAdmin)