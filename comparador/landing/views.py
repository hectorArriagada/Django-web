from django.shortcuts import render

# Create your views here.

def landing(request):
    context = {}
    return render(request, 'pages/landing.html', context)

def productos(request):
    context = {}
    return render(request, 'pages/productos.html', context)

def supermercados(request):
    context = {}
    return render(request, 'pages/supermercados.html', context)

def mapa(request):
    context = {}
    return render(request, 'pages/mapa.html', context)

def login(request):
    context = {}
    return render(request, 'pages/login.html', context)

def registrar(request):
    context = {}
    return render(request, 'pages/registrar.html', context)
