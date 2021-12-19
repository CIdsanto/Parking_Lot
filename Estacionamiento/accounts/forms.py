from django import forms
from django.forms import ModelForm, widgets
from .models import Clientes

class ClienteForm(ModelForm):
    class Meta: 
        model = Clientes 
        fields= "__all__"
        # labels ={
        #     'placa':'',
        #     'tipo':'Hora/Dia',
        #     'slot':'Lugar de Estacionamiento',
        #     'entrada':'',
        #     'salida':'',
        #     'pago':'',


        # }
        # widgets = {
        #     'placa': forms.TextInput(attrs={'class':'input', 'placeholder':'Placa'}),
        #     'entrada': forms.DateField,
        #     'placa': forms.TextInput(attrs={'class':'input', 'placeholder':'Placa'}),
        #     'placa': forms.TextInput(attrs={'class':'input', 'placeholder':'Placa'}),

        # }