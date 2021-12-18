from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('clientes', views.clientes)

]