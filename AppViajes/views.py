from dataclasses import fields
from multiprocessing import AuthenticationError
from django.shortcuts import render
from django.urls import reverse_lazy
from AppViajes.forms import PostForm
from .models import Post, Mensaje
from AppViajes.forms import MensajeFormulario
from django.db.models import Q
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView,DeleteView, UpdateView

# Create your views here.

def inicio(request):
    return render (request, 'AppViajes/inicio.html')


def pages(request):
    busqueda=request.GET.get("buscar")
    posts =Post.objects.filter()
    
    if busqueda:
        posts = Post.objects.filter(
            Q(titulo__icontains = busqueda) |
            Q(contenido__icontains = busqueda) |
            Q(subtitulo__icontains = busqueda)
             ).distinct()

        
    return render(request, 'AppViajes/index.html', {'posts':posts})


def detallepost(request, slug):
    post =Post.objects.get(
        slug = slug
    )
    
    mensajes=Mensaje.objects.filter(dirigido_a=post.id)
   
    #para el formualrio:
    
    if request.method == 'POST':
        miFormulario = MensajeFormulario(request.POST)
        print(miFormulario)
        
        if miFormulario.is_valid:
            usuario= request.user
            mensaje =miFormulario.cleaned_data.get("mensaje")
            Mensaje.objects.create(autor_mensaje=usuario,mensaje=mensaje,dirigido_a= post)

    miFormulario = MensajeFormulario()

    return render(request, 'AppViajes/post.html', {'Detalle_post':post,'mensajes':mensajes, 'miFormulario': miFormulario})
 
class detallemensajes(ListView):
    model=Mensaje
    template_name='AppViajes/mensajes.html'
    fields=['mensaje','autor_mensaje']

    def get_queryset(self):
        return Mensaje.objects.filter(autor_mensaje=self.request.user)


class ListarPost(ListView):
    model = Post
    template_name= 'AppViajes/listar_post.html'
    #queryset= model.objects.all()


class CrearPost(CreateView):
    model= Post
    form_class= PostForm
    template_name= 'AppViajes/crear_post.html'
    success_url = reverse_lazy("AppViajes: listar_post")
   

    