from django.shortcuts import render
from django.http import HttpResponse
from .models import *
# Create your views here.

def home(request):
    Size_Estacionamiento = Size.objects.all()
    Vehiculo = Clientes.objects.all()
    return render(request, 'accounts/dashboard.html', {'Size_Estacionamiento': Size_Estacionamiento, 'Vehiculo' : Vehiculo})

def clientes(request):
    return render(request, 'accounts/clientes.html')

# def info(request):
#     Size_Estacionamiento = Size.objects.all()
#     return render(request, 'accounts/dashboard.html', {'Size_Estacionamiento': Size_Estacionamiento})
# def vehiculo(request):
#     Entrada = Clientes.objects.all()