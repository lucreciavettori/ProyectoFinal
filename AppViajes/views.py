from django.shortcuts import render
from .models import Post
from django.db.models import Q

# Create your views here.

def inicio(request):
    return render (request, 'AppViajes/inicio.html')

def pages(request):
    busqueda=request.GET.get("buscar")
    posts =Post.objects.filter()
    
    if busqueda:
        posts = Post.objects.filter(
            Q(titulo__icontains = busqueda))

        
    return render(request, 'AppViajes/index.html', {'posts':posts})

def detallepost(request, slug):
    post =Post.objects.get(
        slug = slug
    )
    return render(request, 'AppViajes/post.html', {'Detalle_post':post})