from django.shortcuts import render
from django.views.generic import TemplateView , CreateView, UpdateView, DetailView
from django.urls import reverse_lazy
from .forms import ProductoForm
from .models import Producto

class ProductosView(TemplateView):
    template_name = 'productos.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['productos'] = Producto.objects.all()
        return context

class CrearProductoView(CreateView):
    model = Producto
    template_name = 'crear_producto.html'
    form_class = ProductoForm
    success_url = reverse_lazy('productos:productosapp') 

class EditarProductoView(UpdateView):
    model = Producto
    template_name = 'editar_producto.html'
    form_class = ProductoForm
    success_url = reverse_lazy('productos:productosapp') 

class DetalleProductoView(DetailView):
     model = Producto
     template_name = 'detalle_producto.html' 
     context_object_name = 'producto'     

class ListadoProductosView(TemplateView):
    template_name = 'listado_productos.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        vNombre=self.request.GET.get('nombre')
        if vNombre:
            context['productos'] = Producto.objects.filter(nombre__icontains=vNombre)
        else:
            context['productos'] = Producto.objects.all()
        return context