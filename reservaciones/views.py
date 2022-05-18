from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
import reservaciones

from reservaciones.models import Cliente, Habitacion, Reservacion
from reservaciones.forms import *
from reservaciones import utilities

# Create your views here.

def index(request):

    form = PeriodoForm()

    if request.user.is_authenticated:
        cliente = Cliente.objects.filter(usuario = request.user).first()
        if cliente is not None:
            reservaciones = Reservacion.objects.filter(cliente=cliente)
            return render(request, 'index.html', {'form': form, 'reservaciones':reservaciones})
            
    return render(request, 'index.html', {'form': form})

def iniciar_sesion(request):

    if request.user.is_authenticated:
        return redirect('/')
     
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username =username, password = password)
 
        if user is not None:
            login(request,user)
            return redirect('/')
        else:
            form = AuthenticationForm()
            return render(request,'iniciar-sesion.html',{'form':form})
     
    else:
        form = AuthenticationForm()
        return render(request, 'iniciar-sesion.html', {'form':form})

def registro(request):

    if request.method == 'POST':
        form_cliente = ClienteForm(data=request.POST)
        form_usuario = UserCreationForm(request.POST)
        if form_cliente.is_valid() and form_usuario.is_valid():
            username = form_usuario.cleaned_data['username']
            password = form_usuario.cleaned_data['password1']

            usuario = User.objects.create_user(username=username, password=password)
            usuario.save()

            cliente = Cliente(
                usuario= usuario,
                nombre = form_cliente.cleaned_data['nombre'],
                apellido = form_cliente.cleaned_data['apellido'],
                tipo_documento = form_cliente.cleaned_data['tipo_documento'],
                documento = form_cliente.cleaned_data['documento'],
                telefono = form_cliente.cleaned_data['telefono'],
                direccion = form_cliente.cleaned_data['direccion'],
            )
            cliente.save()

            messages.success(request, 'Se ha registrado exitosamete')
            login(request, usuario)
            return redirect('/')
            
        else:
            messages.error(request, 'Los datos suministrados no son validos')
            form_cliente = ClienteForm(request.POST)
            form_usuario = UserCreationForm(request.POST)
            return render(request, 'registro.html', {'form_cliente': form_cliente, 'form_usuario':form_usuario})
        
    form_cliente = ClienteForm()
    form_usuario = UserCreationForm()

    return render(request, 'registro.html', {'form_cliente': form_cliente, 'form_usuario':form_usuario})

def cerrar_sesion(request):
    logout(request)
    return redirect('/')

def habitaciones(request):

    if request.method == 'POST':

        form = PeriodoForm(request.POST)
        if form.is_valid():
            
            fecha_entrada = form.cleaned_data['fecha_entrada']
            fecha_salida = form.cleaned_data['fecha_salida']

            habitaciones = Habitacion.objects.all()
            
            disponibles = utilities.habitaciones_disponibles(habitaciones, fecha_entrada, fecha_salida)

            return render(request, 'listar-habitaciones.html', {'habitaciones':disponibles})

    habitaciones = Habitacion.objects.all()

    return render(request, 'listar-habitaciones.html', {'habitaciones':habitaciones})
    
def habitacion(request, codigo):

    form = ReservacionForm()
    habitacion = Habitacion.objects.filter(codigo=codigo).first()

    return render(request, 'habitacion.html', {'form':form, 'habitacion': habitacion})

def reservar(request, codigo_habitacion):

    if request.method == 'POST':
        form = ReservacionForm(request.POST)
        if form.is_valid():

            fecha_entrada = form.cleaned_data['fecha_entrada']
            fecha_salida = form.cleaned_data['fecha_salida']

            cliente = Cliente.objects.get(usuario=request.user)
            habitacion = Habitacion.objects.get(codigo = codigo_habitacion)
            precio_reserva = habitacion.precio_noche * ((fecha_salida - fecha_entrada).days + 1)
            print("Precio total : ", precio_reserva)

            reservacion = Reservacion(
                cliente = cliente,
                habitacion = habitacion,
                precio_reserva = precio_reserva,
                fecha_entrada = fecha_entrada,
                fecha_salida = fecha_salida
            )

            reservacion.save()

            return redirect('/')
            
    form = ReservacionForm()
    habitacion = Habitacion.objects.get(codigo=codigo_habitacion)

    return render(request, 'habitacion.html', {'form': form, 'habitacion':habitacion})
    