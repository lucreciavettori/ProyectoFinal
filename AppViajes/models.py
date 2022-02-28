from django.db import models

# Creamos la calse "Blog"
class Blog(models.Model):
    titulo=models.CharField(max_length=30)
    subtitulo=models.CharField(max_length=30)
    imagen=models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100)

# Creamos la calse "Usuario"
class Usuario(models.Model):
    nombre=models.CharField(max_length=30)
    apellido=models.CharField(max_length=30)
    nickname=models.CharField(max_length=30)
    email=models.EmailField()
    ciudad=models.CharField(max_length=30)
    edad=models.IntegerField()
    alta=models.DateField()

# Creamos la calse "Mensaje"
class Mensaje(models.Model):
    titulo=models.CharField(max_length=30)
    contenido=models.TextField(max_length=100)
    fecha=models.DateField()
    deNombre=models.CharField(max_length=30)
    deEmail=models.EmailField()
    paraNombre=models.CharField(max_length=30)
    paraEmail=models.EmailField()