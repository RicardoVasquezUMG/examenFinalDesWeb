from django.views.generic import TemplateView, CreateView, UpdateView, DetailView
from django.urls import reverse_lazy
from .models import Publicacion
from .forms import PublicacionForm

class PubliView(TemplateView):
    template_name = 'publicaciones.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['publicaciones'] = Publicacion.objects.all()
        return context

class CrearPublicacionView(CreateView):
    model = Publicacion
    template_name = 'crear_publicacion.html'
    form_class = PublicacionForm
    success_url = reverse_lazy('publicaciones:publiapp')


class EditarPublicacionView(UpdateView):
    model = Publicacion
    template_name = 'editar_publicacion.html'
    form_class = PublicacionForm
    success_url = reverse_lazy('publicaciones:publiapp')    



class DetallePublicacionView(DetailView):
     model = Publicacion
     template_name = 'detalle_publicaciones.html' 
     context_object_name = 'publicacion'  

class ListadoPublicacionView(TemplateView):
    template_name = 'listado_publicaciones.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        vNombre=self.request.GET.get('titulo')
        if vNombre:
            context['publicaciones'] = Publicacion.objects.filter(titulo__icontains=vNombre)
        else:
            context['publicaciones'] = Publicacion.objects.all()
        return context