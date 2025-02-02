from django.shortcuts import render
from .models import Genero, Usuario, Carrito
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create your views here.

# Vistas Principales
##############################################################

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



##############################################################




# CRUD Usuarios
##############################################################

# Vista crud
@login_required
def crud(request):
    usuarios = Usuario.objects.all()
    context = {
        "usuarios": usuarios
    }
    return render(request, 'pages/crud.html', context)


# Vista CRUD Agregar
def registrar(request):
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
        genero = request.POST["genero"]
        correo = request.POST["correo"]
        telefono = request.POST["telefono"]

        objGenero = Genero.objects.get(id_genero=genero)

        obj = Usuario.objects.create(
            rut=rut,
            nombre=nombre,
            appaterno=appaterno,
            apmaterno=apmaterno,
            clave=clave,
            fecnac=fecnac,
            edad=edad,
            genero=objGenero,
            correo=correo,
            telefono=telefono,
        )

        obj.save()
        context = {'mensaje': 'Datos guardados',
        }
        return render(request, 'pages/registrar.html', context)


# Vista CRUD Eliminar
def user_del(request, pk):
    try:
        usuario = Usuario.objects.get(rut=pk)
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

        return render(request, 'pages/crud.html', context)


# Vista CRUD Buscar
def user_find(request,pk):
    if pk != "":
        usuario = Usuario.objects.get(rut=pk)
        generos = Genero.objects.all()
        context = {
            "usuario": usuario,
            "generos": generos,
        }
        
        return render(request, 'pages/user_update.html', context)

    else:
        usuarios = Usuario.objects.all()
        context = {
            "mensaje": "Error, Rut no encontrado...",
            "usuarios": usuarios,
        }

        return render(request, 'pages/crud.html', context)


# Vista CRUD Actualizar
def user_update(request):
    if request.method !="POST":
        rut = request.POST["rut"]
        nombre = request.POST["nombre"]
        appaterno = request.POST["appaterno"]
        apmaterno = request.POST["apmaterno"]
        clave = request.POST["clave"]
        fecnac = request.POST["fechanac"]
        edad = request.POST["edad"]
        genero = request.POST["genero"]
        correo = request.POST["correo"]
        telefono = request.POST["telefono"]

        objGenero = Genero.objects.get(id_genero=genero)

        obj = Usuario(
            rut=rut,
            nombre=nombre,
            appaterno=appaterno,
            apmaterno=apmaterno,
            clave=clave,
            fecnac=fecnac,
            edad=edad,
            genero=objGenero,
            correo=correo,
            telefono=telefono,
        )

        obj.save()

        generos = Genero.objects.all()
        context = {
            "mensaje": "Modificado con exito",
            "generos": generos,
            "usuario": obj,
        }
        
        return render(request, "pages/user_update.html", context)
    

##############################################################



# CRUD Carrito
##############################################################

# Vista CRUD

# Vista CRUD agregar

# Vista CRUD eliminar

# Vista CRUD buscar

# Vista CRUD modificar


##############################################################



# Sesiones
##############################################################

# Vista para conectar
def conectar(request):
    if request.method == "POST":
        email = request.POST["username"]
        password = request.POST["pass"]
        us = User.objects.get(email=email)

        user = authenticate(request, username=us.username, password=password)
        if user is not None:
            login(request, user)
            print("conectado")
            return render(request, "pages/landing.html", context)
        
        else:
            context = {
                "mensaje": "Usuario o contraseña incorrecta",
                "design": "alert alert-danger w-50 mx-auto text-center", 
            }
            return render(request, "pages/login.html")
    
    else:
        context = {}
        return render(request, 'pages/login.html', context)
    

# Vista para desconectar
def desconectar(request):
    logout(request)
    context = {
        "mensaje": "Sesion cerrada",
        "design": "alert alert-info w-50 mx-auto text-center"
    }
    return render(request, 'pages/login.html', context)