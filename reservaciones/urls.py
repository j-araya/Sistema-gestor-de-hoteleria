from atexit import register
from operator import index
from unicodedata import name
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("iniciar-sesion", views.iniciar_sesion, name="iniciar-sesion"),
    path("registro", views.registro, name="registro"),
    path('cerrar-sesion', views.cerrar_sesion, name='cerrar-sesion'),

]