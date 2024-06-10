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
    path('user_add', views.user_add, name='user_add'),
    path('user_del/<str:pk>', views.user_del, name='user_del'),
    path('user_find/<str:pk>', views.user_find, name='user_find'),
    #path('user_update', views.user_update, name='user_update'),
    ]