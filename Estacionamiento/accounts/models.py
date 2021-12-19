from django.db import models
from django.db.models.deletion import DO_NOTHING

# Create your models here.
class Size(models.Model):
    espacios = models.IntegerField('Espacios Totales')
    def __str__(self):
        return str(self.espacios)

class Tipo(models.Model):
    name = models.CharField('Tipo Estacionamiento', max_length=50)
    def __str__(self):
        return self.name

class Clientes(models.Model):
    placa = models.CharField('Numero Placa', max_length=120)
    # tipo = models.CharField(max_length=120)
    tipo = models.ForeignKey(Tipo, blank=True, null =True, on_delete=DO_NOTHING)
    slot = models.ForeignKey(Size, blank=True, null =True, on_delete=DO_NOTHING)
    entrada = models.DateTimeField('Entrada', blank=True, null=True)
    salida = models.DateTimeField('Salida', blank=True, null=True)
    pago = models.CharField(max_length=120, blank=True)

    def __str__(self):
        return self.placa
# class Salidas(models.Model):
#     # placa 
#     def __str__(self):
#         return self.name