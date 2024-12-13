from django.db import models

class Producto(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to='media/productos/', default='productos/default_image.jpg')
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    es_skin = models.BooleanField(default=False)

    def __str__(self):
        return self.nombre




