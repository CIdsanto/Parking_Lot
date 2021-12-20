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
        widgets = {
            # 'placa': forms.TextInput(attrs={'class':'input', 'placeholder':'Placa'}),
            'entrada': forms.TextInput(attrs={ 'value':'06.10.2017 20:12:45', 'size':'19', 'onClick':'xCal(this, {lang: "en", order: 1})', 'onKeyUp':'xCal()', }),
            'salida': forms.TextInput(attrs={ 'value':'06.10.2017 20:12:45', 'size':'19', 'onClick':'xCal(this)', 'onKeyUp':'xCal()', }),

            # 'placa': forms.TextInput(attrs={'class':'input', 'placeholder':'Placa'}),

        }