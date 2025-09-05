
# Create your models here.

from django.db import models

class Administrador(models.Model):
	nombre = models.CharField(max_length=100)
	apellido = models.CharField(max_length=100)
	edad = models.PositiveIntegerField()
	cargo = models.CharField(max_length=50)
	departamento = models.CharField(max_length=50)
	correo = models.EmailField(unique=True)
	telefono = models.CharField(max_length=20)
	ciudad = models.CharField(max_length=50)

	def __str__(self):
		return f"{self.nombre} {self.apellido}"
