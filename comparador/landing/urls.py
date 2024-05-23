from django.urls import path
from . import views

""" path('nombreURL',funcionVista,nombreDePagina) """
urlpatterns = [
    path("", views.landing, name="landing"),
]