from django.contrib import admin
from django.urls import path,include
from Apps.PRODUCTOS import views
from .views import ProductosView, CrearProductoView, EditarProductoView, DetalleProductoView, ListadoProductosView

app_name='productos'
urlpatterns = [
    path('',ProductosView.as_view(), name='productosapp'),
    path('crear/',CrearProductoView.as_view(), name='crear'),
    path('editar/<int:pk>/',EditarProductoView.as_view(), name='editar'),
    path('detalle/<int:pk>/', DetalleProductoView.as_view(), name='detalle'),
    path('listado/', ListadoProductosView.as_view(), name='listado'),
]