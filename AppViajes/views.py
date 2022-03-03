from django.shortcuts import render
from .models import Post

# Create your views here.

def inicio(request):
    return render (request, 'AppViajes/inicio.html')

def pages(request):
    posts =Post.objects.filter()
    return render(request, 'AppViajes/index.html', {'posts':posts})

def detallepost(request, slug):
    post =Post.objects.get(
        slug = slug
    )
    return render(request, 'AppViajes/post.html', {'Detalle_post':post})