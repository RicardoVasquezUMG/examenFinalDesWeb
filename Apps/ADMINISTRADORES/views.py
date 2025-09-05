from django.views.generic import TemplateView, CreateView, UpdateView, DetailView
from django.urls import reverse_lazy
from .models import Administrador
from .forms import AdministradorForm

class AdminView(TemplateView):
    template_name = 'administradores.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['administradores'] = Administrador.objects.all()
        return context

class CrearAdministradorView(CreateView):
    model = Administrador
    template_name = 'crear_administrador.html'
    form_class = AdministradorForm
    success_url = reverse_lazy('adminis:adminapp')

class EditarAdministradorView(UpdateView):
    model = Administrador
    template_name = 'editar_administrador.html'
    form_class = AdministradorForm
    success_url = reverse_lazy('adminis:adminapp')


class DetalleAdministradorView(DetailView):
     model = Administrador
     template_name = 'detalle_administradores.html' 
     context_object_name = 'administrador'

class ListadoAdministradoresView(TemplateView):
    template_name = 'listado_administradores.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        vNombre=self.request.GET.get('nombre')
        if vNombre:
            context['administradores'] = Administrador.objects.filter(nombre__icontains=vNombre)
        else:
            context['administradores'] = Administrador.objects.all()
        return context
