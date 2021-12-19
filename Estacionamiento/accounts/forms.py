from django import forms
from django.forms import ModelForm
from .models import Clientes

class ClienteForm(ModelForm):
    class Meta: 
        model = Clientes 
        fields= "__all__"
        