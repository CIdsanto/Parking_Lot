from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.http import HttpResponseRedirect
from .forms import ClienteForm
from django.db.models import Q 
# Create your views here.

def home(request):
    Size_Estacionamiento = Size.objects.all()
    Vehiculo = Clientes.objects.all()
    # placa_cliente = Clientes.objects.get(pk= cliente_id)
    return render(request, 'accounts/dashboard.html', {'Size_Estacionamiento': Size_Estacionamiento, 'Vehiculo' : Vehiculo})

def pagos(request):
    estacionados= Clientes.objects.all()
    return render(request, 'accounts/incomes.html', {'estacionados': estacionados} )

def mostrar_pagos(request, cliente_id):
    placa_cliente = Clientes.objects.get(pk= cliente_id)
    # Vehiculo = Clientes.objects.all()

    return render(request, 'accounts/mostrar_pagos.html', {'placa_cliente': placa_cliente } )

def search_vehiculo(request):
    if request.method == "POST":
        searched = request.POST['searched']
        vehiculo = Clientes.objects.filter(placa__contains =searched) 
        # tipo = Clientes.objects.filter(tipo__contains =searched) 
        
        return render(request, 'accounts/search.html', {'searched': searched, 'vehiculo': vehiculo, } )
    else: 
        return render(request, 'accounts/search.html', {} )

    

def clientes(request):
    submitted = False
    if request.method == "POST":
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/clientes?submitted=True')
    else:
        form = ClienteForm
        if 'submitted' in request.GET:
            submitted = True 
    return render(request, 'accounts/clientes.html', {'form': form, 'submitted':submitted})


# def info(request):
#     Size_Estacionamiento = Size.objects.all()
#     return render(request, 'accounts/dashboard.html', {'Size_Estacionamiento': Size_Estacionamiento})
# def vehiculo(request):
#     Entrada = Clientes.objects.all()