from django.shortcuts import render
from .models import Post, Mensaje
from AppViajes.forms import MensajeFormulario
from django.db.models import Q
from django.views.generic.edit import FormMixin

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
            destinatario=Post.objects.filter(titulo=post.titulo)
            mensaje= Mensaje.objects.create(autor_mensaje=usuario,mensaje=mensaje, dirigido_a=destinatario)
        else:
            return super().form_invalid(miFormulario)
        return super().form_valid(miFormulario)
    miFormulario = MensajeFormulario()

    return render(request, 'AppViajes/post.html', {'Detalle_post':post,'mensajes':mensajes, 'miFormulario': miFormulario})

    
def detallemensajes(request):

    return render(request, 'AppViajes/mensajes.html')  




