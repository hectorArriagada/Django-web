from django.db import models

# Create your models here.

# modelo para el genero
class Genero(models.Model):
    id_genero = models.AutoField(db_column='idGenero', primary_key=True)
    genero = models.CharField(max_length=20, blank=False, null=False)


# modelo para el usuario
class Usuario(models.Model):
    rut = models.CharField(primary_key=True, max_length=10)
    nombre = models.CharField(max_length=30)
    appaterno = models.CharField(max_length=30)
    apmaterno = models.CharField(max_length=30)
    clave = models.CharField(max_length=30)
    fecnac = models.DateField(blank=False, null=False)
    edad = models.IntegerField()
    genero = models.ForeignKey('Genero', on_delete=models.CASCADE, db_column='idGenero')
    correo = models.EmailField(unique=True, max_length=100, blank=True, null=True)
    telefono = models.IntegerField()


# Modelo para el carrito
class Carrito(models.Model):
    id_producto = models.CharField(primary_key=True, max_length=20)
    producto = models.CharField(max_length=100)
    precio = models.IntegerField()
    cantidad = models.IntegerField()
    tienda = models.CharField(max_length=30)
    url = models.CharField(max_length=500)