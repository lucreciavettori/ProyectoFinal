from dataclasses import fields
from multiprocessing import AuthenticationError
from django.shortcuts import render
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
    
    #para la barra de busqueda:

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
    
    mensajes=Mensaje.objects.filter(dirigido_a=post.id).order_by('fecha_creacion_mensaje')
   
    #para enviar mensaje a traves de formulario:
    
    if request.method == 'POST':
        miFormulario = MensajeFormulario(request.POST)
        print(miFormulario)
        
        if miFormulario.is_valid:
            usuario= request.user
            mensaje =miFormulario.cleaned_data.get("mensaje")
            mensaje= Mensaje.objects.create(autor_mensaje=usuario,mensaje=mensaje,dirigido_a=post)
    miFormulario = MensajeFormulario()

    return render(request, 'AppViajes/post.html', {'Detalle_post':post,'mensajes':mensajes, 'miFormulario': miFormulario})

class detallemensajes(ListView):
    model = Mensaje
    template_name = 'AppViajes/mensajes.html'

    def get(self, request, *args, **kwargs):
        self.queryset = Mensaje.objects.filter(dirigido_a__autor=request.user).order_by('fecha_creacion_mensaje')
        self.object_list = self.get_queryset()
        context = self.get_context_data()
        return self.render_to_response(context)

def about(request):
    return render (request, 'AppViajes/about.html')



    