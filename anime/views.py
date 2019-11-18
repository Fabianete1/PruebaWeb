from django.shortcuts import render
from .models import Usuario

def index_list(request):
    return render(request,
     'index.html',)

def anime_list(request):
    return render(request, 
    'Anime.html', {}) 

def galeria_list(request):
    return render(request, 
    'Galeria.html', {}) 

def manga_list(request):
    return render(request, 
    'Manga.html', {})

def nosotros_list(request):
    return render(request, 
    'Nosotros.html', {})

def objeto_list(request):
    return render(request,
     'Objeto.html', {})

def registro_list(request):
    return render(request, 
    'Resgistro.html', {})