from django.db import models

from django.contrib.auth.models import User

# Create your models here.

class Cliente(models.Model):

    TIPOS_DOCUMENTOS = [
        ('V','V'),
        ('J','J'),
        ('E','E'),
    ]

    usuario = models.OneToOneField(User, on_delete=models.CASCADE)

    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    tipo_documento = models.CharField(max_length=100, choices=TIPOS_DOCUMENTOS)
    documento = models.CharField(max_length=100)
    telefono = models.CharField(max_length=100)
    direccion = models.TextField(max_length=500)

    def __str__(self):
        return "{} {}".format(self.nombre, self.apellido)
        

class Habitacion(models.Model):

    codigo = models.IntegerField(unique=True)
    descripcion = models.CharField(max_length=100)
    precio_noche = models.FloatField()
    camas_matrimoniales = models.IntegerField()
    camas_individuales = models.IntegerField()

    def __str__(self):
        return "{} - {}".format(self.codigo, self.descripcion)

class Reservacion(models.Model):

    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    habitacion = models.ForeignKey(Habitacion, on_delete=models.CASCADE)
    precio_reserva = models.FloatField()
    fecha_entrada = models.DateField()
    fecha_salida = models.DateField()
    fecha_registro = models.DateField(auto_now_add=True)

    def __str__(self):
        return "{} {} {} {}".format(self.habitacion.codigo, self.cliente, self.fecha_entrada, self.fecha_salida)
        