from django.db import models
# Create your models here.


class Proyecto(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=250)
    imagen = models.ImageField(upload_to='portafolio/imagenes/')
    url = models.URLField(blank=True)
