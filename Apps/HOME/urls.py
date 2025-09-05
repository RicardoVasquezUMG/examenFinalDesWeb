from django.contrib import admin
from django.urls import path,include
from Apps.HOME import views
from .views import HomeView, RegistroView, LoginView
from django.contrib.auth.views import LogoutView

app_name='home'
urlpatterns = [
    path('',HomeView.as_view(), name='homeapp'),
    path('registro/', RegistroView.as_view(), name='registro'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
