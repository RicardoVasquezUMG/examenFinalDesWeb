from django.views.generic import TemplateView, CreateView, UpdateView, DetailView
from django.urls import reverse_lazy
from .models import Categoria
from .forms import CategoriaForm

class CategoriaView(TemplateView):
    template_name = 'categorias.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categorias'] = Categoria.objects.all()
        return context

class CrearCategoriaView(CreateView):
    model = Categoria
    template_name = 'crear_categoria.html'
    form_class = CategoriaForm
    success_url = reverse_lazy('categorias:categoriaapp')

class EditarCategoriaView(UpdateView):
    model = Categoria
    template_name = 'editar_categoria.html'
    form_class = CategoriaForm
    success_url = reverse_lazy('categorias:categoriaapp')

class DetalleCategoriaView(DetailView):
     model = Categoria
     template_name = 'detalle_categoria.html' 
     context_object_name = 'categoria'

class ListadoCategoriasView(TemplateView):
    template_name = 'listado_categorias.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        vNombre=self.request.GET.get('nombre')
        if vNombre:
            context['categorias'] = Categoria.objects.filter(nombre__icontains=vNombre)
        else:
            context['categorias'] = Categoria.objects.all()
        return context
