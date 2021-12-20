from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('clientes', views.clientes, name='clientes'),
    path('pagos', views.pagos, name='pagos'),
    path('mostrar_pagos/<cliente_id>', views.mostrar_pagos, name='mostrar-pagos'),
    path('search_vehiculo', views.search_vehiculo, name='search'),


    
]

