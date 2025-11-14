from django.contrib import admin
from django.urls import path,include
from Apps.CATEGORIAS import views

from .views import CategoriaView, CrearCategoriaView, EditarCategoriaView, DetalleCategoriaView, ListadoCategoriasView

app_name='categorias'
urlpatterns = [
    path('', CategoriaView.as_view(), name='categoriaapp'),
    path('crear/', CrearCategoriaView.as_view(), name='crear'),
    path('editar/<int:pk>/', EditarCategoriaView.as_view(), name='editar'),
    path('detalle/<int:pk>/', DetalleCategoriaView.as_view(), name='detalle'),
    path('listado/', ListadoCategoriasView.as_view(), name='listado'),
]

