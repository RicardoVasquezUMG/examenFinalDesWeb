from django.shortcuts import render
from django.views.generic import TemplateView , CreateView, UpdateView, DetailView
from django.urls import reverse_lazy
from .forms import EstudianteForm
from .models import Estudiante

# Create your views here.
class EstudiantesView(TemplateView):
    template_name = 'estudiantes.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['estudiantes'] = Estudiante.objects.all()
        return context
    
class CrearEstudianteView(CreateView):
    model = Estudiante
    template_name = 'crear_estudiante.html'
    form_class = EstudianteForm
    success_url = reverse_lazy('student:Estudiantesapp') 

class EditarEstudianteView(UpdateView):
    model = Estudiante
    template_name = 'editar_estudiante.html'
    form_class = EstudianteForm
    success_url = reverse_lazy('student:Estudiantesapp') 

class DetalleEstudianteView(DetailView):
     model = Estudiante
     template_name = 'detalle_estudiantes.html' 
     context_object_name = 'estudiante'     

class ListadoEstudiantesView(TemplateView):
    template_name = 'listado_estudiantes.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        vNombre=self.request.GET.get('nombre')
        if vNombre:
            context['estudiantes'] = Estudiante.objects.filter(nombre__icontains=vNombre)
        else:
            context['estudiantes'] = Estudiante.objects.all()
        return context