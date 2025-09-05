from django.contrib import admin
from django.urls import path,include
from Apps.ABOUT import views
from .views import AboutView

app_name='about'
urlpatterns = [
    path('',AboutView.as_view(), name='aboutapp')
]
