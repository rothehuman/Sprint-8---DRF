from django.urls import path
from . import views

urlpatterns = [
    path('clientes/<int:cliente_id>/', views.ClientesById.as_view()),
    path('cuentas/<int:cliente_id>/', views.CuentasById.as_view()),
    path('prestamos/<int:cliente_id>/', views.PrestamosById.as_view()), 
    path('prestamosSucursal/<int:sucursal_id>/', views.PrestamosSucursalById.as_view()),     
    path('tarjetas/<int:cliente_id>/', views.TarjetasById.as_view()),
    path('direcciones/<int:address_id>/', views.DireccionesById.as_view()),       
    path('prestamos/', views.Prestamos.as_view()), 
    path('sucursales/', views.Sucursales.as_view()),   
]