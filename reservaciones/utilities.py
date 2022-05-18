from datetime import datetime


from datetime import datetime

from reservaciones.models import *

def esta_disponible(habitacion, fecha_entrada, fecha_salida):
    
    reservaciones = Reservacion.objects.filter(habitacion=habitacion)

    for reserva in reservaciones:
        if not(fecha_entrada > reserva.fecha_salida or fecha_salida < reserva.fecha_entrada):
            return False

    return True

def habitaciones_disponibles(habitaciones, fecha_entrada, fecha_salida):

    disponibles = []

    for habitacion in habitaciones:
        if esta_disponible(habitacion, fecha_entrada, fecha_salida):
            disponibles.append(habitacion)
        
    return disponibles
