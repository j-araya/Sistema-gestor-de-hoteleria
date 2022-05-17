from email import message
import re
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from reservaciones.models import Cliente
from reservaciones.forms import *


# Create your views here.

def index(request):
    
    return render(request, 'index.html', {})

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
    
login_required('/', 'iniciar-sesion')
def cerrar_sesion(request):
    logout(request)
    return redirect('/')