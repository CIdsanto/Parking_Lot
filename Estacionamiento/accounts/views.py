from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return render(request, 'accounts/dashboard.html')

def clientes(request):
    return render(request, 'accounts/clientes.html')