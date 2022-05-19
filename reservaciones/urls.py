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

    path('habitaciones', views.habitaciones, name='habitaciones'),
    path('habitacion/<int:codigo>', views.habitacion, name='habitacion'),

    path('reservar/<int:codigo_habitacion>', views.reservar, name='reservar'),
    path('reservacion/<int:id>', views.reservacion, name='reservacion'),
    path('eliminar/reservacion/<int:id>', views.eliminar_reservacion, name='eliminar-reservacion'),

]