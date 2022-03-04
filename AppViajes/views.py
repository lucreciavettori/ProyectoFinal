from django.shortcuts import render
from .models import Post, Mensaje
from AppViajes.forms import MensajeFormulario
from django.db.models import Q

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
    mensajes=["hola","buen dia"]
   
    if request.method == 'POST':
        
        miFormulario = MensajeFormulario(request.POST)
        
        print(miFormulario)
        
        if miFormulario.is_valid:
            
            informacion = miFormulario.data
            
            r_autor = informacion['autor']
            r_mensaje = informacion['mensaje']
        
            mensaje= Mensaje(autor_mensaje=r_autor, mensaje=r_mensaje)
            mensaje.save()
    
    miFormulario = MensajeFormulario()

    return render(request, 'AppViajes/post.html', {'Detalle_post':post,'mensajes':mensajes,'miFormulario': miFormulario})


    

    
