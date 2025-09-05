
# Create your models here.

from django.db import models

from Apps.ESTUDIANTES.models import Estudiante
from Apps.ADMINISTRADORES.models import Administrador

class Publicacion(models.Model):
	titulo = models.CharField(max_length=200)
	autor = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
	fecha = models.DateField()
	administrador = models.ForeignKey(Administrador, on_delete=models.CASCADE)
	estado = models.CharField(max_length=20)

	def __str__(self):
		return self.titulo
