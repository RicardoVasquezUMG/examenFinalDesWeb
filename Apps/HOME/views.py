from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from Apps.HOME.forms import RegistroForm
from django.contrib.auth.views import LoginView


from Apps.HOME.models import Usuario

class HomeView(TemplateView):
    template_name = 'home.html'

class RegistroView(CreateView):
    template_name = 'registro.html'
    model = Usuario
    form_class = RegistroForm
    success_url = reverse_lazy('home:homeapp')

class LoginView(LoginView):
    template_name = 'login.html'
    success_url = reverse_lazy('home:homeapp')
