from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User

class Post(models.Model):
    id=models.AutoField(primary_key= True)
    titulo=models.CharField('Titulo',max_length=50,null= False, blank= False)
    subtitulo=models.CharField('Subtitulo',max_length=30)
    slug=models.CharField('Slug',max_length=100,null= False, blank= False)
    contenido=RichTextField()
    #imagen=models.ImageField('Imagen Referencial', upload_to= 'imagenes_post/', null= True, blank= True)
    #imagen=models.URLField(max_length=300, null= False, blank= False)
    autor=models.ForeignKey(User, on_delete=models.CASCADE)
    fecha_creacion=models.DateField('Fecha de creación', auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.titulo

class Mensaje(models.Model):
    id=models.AutoField(primary_key= True)
    autor_mensaje=models.ForeignKey(User, on_delete=models.CASCADE)
    mensaje=RichTextField()
    dirigido_a=models.ForeignKey(Post, on_delete=models.CASCADE)
    fecha_creacion_mensaje=models.DateField('Fecha de creación', auto_now=False, auto_now_add=True)
    

    def __str__(self):
        return self.mensaje