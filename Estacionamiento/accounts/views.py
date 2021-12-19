from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.http import HttpResponseRedirect
from .forms import ClienteForm
# Create your views here.

def home(request):
    Size_Estacionamiento = Size.objects.all()
    Vehiculo = Clientes.objects.all()
    return render(request, 'accounts/dashboard.html', {'Size_Estacionamiento': Size_Estacionamiento, 'Vehiculo' : Vehiculo})

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