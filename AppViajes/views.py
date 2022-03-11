from dataclasses import fields
from multiprocessing import AuthenticationError
from turtle import pos
from django.shortcuts import  redirect, render

from .models import Post, Mensaje
from AppViajes.forms import MensajeFormulario, PostForm
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
    #queryset= Post.objects.filter(autor=request.user)
    def get(self, request, *args, **kwargs):
        self.queryset = Post.objects.filter(autor=request.user)
        self.object_list = self.get_queryset()
        context = self.get_context_data()
        return self.render_to_response(context)

class CrearPost(CreateView):
    model= Post
    form_class= PostForm
    success_url = '/AppViajes/listar_post'

class EditarPost(UpdateView):
    model= Post
    template_name= 'AppViajes/post_form.html'
    form_class= PostForm
    success_url = '/AppViajes/listar_post'

class EliminarPost(DeleteView):
    model= Post

    def post (self, request, pk, *args, **kargs):
        object= Post.objects.get(id=pk)
        object.save()
        return redirect ('AppViajes:listar_post')
            


class CrearMensaje(CreateView):
    model= Mensaje
    success_url = '/AppViajes/Detalle_post'
    fields= ['mensaje']


   

    