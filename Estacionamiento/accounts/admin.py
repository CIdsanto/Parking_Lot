from django.contrib import admin
from .models import Tipo
from .models import Clientes
from .models import Size
from .models import Estatus


# from .models import Salidas
admin.site.register(Size)
admin.site.register(Tipo)
admin.site.register(Estatus)
# admin.site.register(Salidas)

@admin.register(Clientes)
class ClientesAdmin(admin.ModelAdmin):
    list_display = ('placa', 'slot', 'tipo', 'entrada')
    ordering = ('placa',)
    search_fields = ('placa', 'entrada', 'tipo__name')
    list_filter = ('tipo__name',)