#from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing, name='landing'),
    path('productos', views.productos, name="productos"),
    path('supermercados', views.supermercados, name="supermercados"),
    path('mapa', views.mapa, name="mapa"),
    path('login', views.login, name="login"),
    path('registrar', views.registrar, name="registrar"),
    path('usuario_add', views.usuario_add, name='usuario_add'),
    ]