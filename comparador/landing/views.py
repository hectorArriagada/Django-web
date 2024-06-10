from django.shortcuts import render
from .models import Genero, Usuario, Carrito

# Create your views here.

# Vista Principal
def landing(request):
    context = {}
    return render(request, 'pages/landing.html', context)

# Vista Productos
def productos(request):
    context = {}
    return render(request, 'pages/productos.html', context)

# Vista Supermercados
def supermercados(request):
    context = {}
    return render(request, 'pages/supermercados.html', context)

# Vista Mapa
def mapa(request):
    context = {}
    return render(request, 'pages/mapa.html', context)

# Vista Login
def login(request):
    context = {}
    return render(request, 'pages/login.html', context)

# Vista Registrar
def registrar(request):
    context = {}
    return render(request, 'pages/registrar.html', context)

# Vista CRUD Agregar
def user_add(request):
    if request.method != 'POST':
        generos = Genero.objects.all()
        context = {
            'generos': generos,
        }
        return render(request, 'pages/registrar.html', context)
    
    else:
        rut = request.POST["rut"]
        nombre = request.POST["nombre"]
        appaterno = request.POST["appaterno"]
        apmaterno = request.POST["apmaterno"]
        clave = request.POST["clave"]
        fecnac = request.POST["fechanac"]
        edad = request.POST["edad"]
        genero = request.POST["optGenero"]
        correo = request.POST["correo"]
        telefono = request.POST["telefono"]

        obj = Usuario.objects.create(
            rut=rut,
            nombre=nombre,
            appaterno=appaterno,
            apmaterno=apmaterno,
            clave=clave,
            fecnac=fecnac,
            edad=edad,
            genero=genero,
            correo=correo,
            telefono=telefono
        )

        obj.save()
        context = {'mensaje': 'Datos guardados'}
        return render(request, 'pages/registrar.html', context)


# Vista CRUD Eliminar
def user_del(request, pk):
    try:
        usuario = Usuario.objets.get(rut=pk)
        usuario.delete()

        usuarios = Usuario.objects.all()
        context = {
            "mensaje": "Registro eliminado con exito",
            "usuarios": usuarios
        }

        return render(request, 'pages/crud.html', context)

    except:
        usuarios = Usuario.objects.all()
        context = {
            "mensaje": "Error, Rut no encontrado...",
            "usuarios": usuarios
        }

        return render(request, 'pages/user_del', context)


# Vista CRUD Buscar
def user_find(request,pk):
    if pk != "":
        usuario = Usuario.objets.get(rut=pk)
        generos = Genero.objets.all()
        context = {
            "usuario": usuario,
            "generos": generos
        }
        
        return render(request, 'pages/user_update.html', context)

    else:
        usuarios = Usuario.objets.all()
        context = {
            "mensaje": "Error, Rut no encontrado...",
            "usuarios": usuarios,
        }

        return render(request, 'pages/user_update.html', context)


# Vista CRUD Actualizar


