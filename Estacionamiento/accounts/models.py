from django.db import models
from django.db.models.deletion import DO_NOTHING

# Create your models here.
class Size(models.Model):
    espacios = models.CharField('Espacios Totales', max_length= 67)

class Tipo(models.Model):
    name = models.CharField('Tipo Estacionamiento', max_length=50)
 

class Clientes(models.Model):
    placa = models.CharField('Numero Placa', max_length=120)
    # tipo = models.CharField(max_length=120)
    tipo = models.ForeignKey(Tipo, blank=True, null =True, on_delete=DO_NOTHING)
    slot = models.ForeignKey(Size, blank=True, null =True, on_delete=DO_NOTHING)
    pago = models.CharField(max_length=120, blank=True)

    def __str__(self):
        return self.placa
# class Salidas(models.Model):
#     # placa 
#     def __str__(self):
#         return self.name