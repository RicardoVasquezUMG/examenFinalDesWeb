from django.db import models
from Apps.CATEGORIAS.models import Categoria

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    stock = models.PositiveIntegerField()
    imagen = models.CharField(max_length=255)  # URL de la imagen

    def __str__(self):
        return self.nombre