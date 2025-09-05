from django.contrib import admin
from django.urls import path,include
from Apps.ESTUDIANTES import views
from .views import EstudiantesView, CrearEstudianteView, EditarEstudianteView, DetalleEstudianteView, ListadoEstudiantesView

app_name='student'
urlpatterns = [
    path('',EstudiantesView.as_view(), name='Estudiantesapp'),
    path('crear/',CrearEstudianteView.as_view(), name='crear'),
    path('editar/<int:pk>/',EditarEstudianteView.as_view(), name='editar'),
    path('detalle/<int:pk>/', DetalleEstudianteView.as_view(), name='detalle'),
    path('listado/', ListadoEstudiantesView.as_view(), name='listado'),
]