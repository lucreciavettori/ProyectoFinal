from django.db import models
from ckeditor.fields import RichTextField
from django.forms import Textarea

class Usuario(models.Model):
    id=models.AutoField(primary_key= True)
    nombre_usuario=models.CharField('Nombre de usuario', max_length=30, null= False, blank= False)
    apellido_usuario=models.CharField('Apellido de usuario', max_length=30, null= False, blank= False)
    #nickname=models.CharField(max_length=30)
    email=models.EmailField('Correo electronico',null= False, blank= False)
    #ciudad=models.CharField(max_length=30)
    #edad=models.IntegerField()
    #alta=models.DateField()

    def __str__(self):
        return "{0},{1}".format(self.apellido_usuario, self.nombre_usuario)

class Post(models.Model):
    id=models.AutoField(primary_key= True)
    titulo=models.CharField('Titulo',max_length=50,null= False, blank= False)
    subtitulo=models.CharField('Subtitulo',max_length=30)
    slug=models.CharField('Slug',max_length=100,null= False, blank= False)
    contenido=RichTextField()
    imagen=models.ImageField('Imagen Referencial', upload_to= 'imagenes_post/')
    #imagen=models.URLField(max_length=300, null= False, blank= False)
    autor=models.ForeignKey(Usuario, on_delete=models.CASCADE)
    fecha_creacion=models.DateField('Fecha de creación', auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.titulo

class Mensaje(models.Model):
    id=models.AutoField(primary_key= True)
    autor_mensaje=models.ForeignKey(Usuario, on_delete=models.CASCADE)
    mensaje=models.TextField('Mensaje',max_length=100,null= False, blank= False)
    dirigido_a=models.ForeignKey(Post, on_delete=models.CASCADE)
    fecha_creacion_mensaje=models.DateField('Fecha de creación', auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.mensaje