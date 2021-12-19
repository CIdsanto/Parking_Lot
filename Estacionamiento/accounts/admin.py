from django.contrib import admin
from .models import Tipo
from .models import Clientes
from .models import Size

# from .models import Salidas
admin.site.register(Size)
admin.site.register(Tipo)
admin.site.register(Clientes)
# admin.site.register(Salidas)
