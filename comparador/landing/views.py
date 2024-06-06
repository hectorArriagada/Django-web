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

def usuario_add(request):
    if request.method != 'POST':
        generos = Genero.objects.all()
        context = {
            'generos': generos
        }
        return render(request, 'pages/usuario_add.html', context)
    
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
        return render(request, 'usuario_add.html', context)