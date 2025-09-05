from django.contrib import admin
from django.urls import path,include
from Apps.ADMINISTRADORES import views

from .views import AdminView, CrearAdministradorView , EditarAdministradorView, DetalleAdministradorView

app_name='adminis'
urlpatterns = [
    path('', AdminView.as_view(), name='adminapp'),
    path('crear/', CrearAdministradorView.as_view(), name='crear'),
    path('editar/<int:pk>/', EditarAdministradorView.as_view(), name='editar'),
    path('detalle/<int:pk>/', views.DetalleAdministradorView.as_view(), name='detalle'),
    path('listado/', views.ListadoAdministradoresView.as_view(), name='listado'),
]

