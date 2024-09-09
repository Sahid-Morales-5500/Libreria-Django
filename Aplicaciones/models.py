from django.db import models

# Create your models here.
class Libro(models.Model):
    Titulo = models.CharField(max_length=200)
    Descripcion = models.TextField()
    Genero = models.CharField(max_length = 30)
    ID = models.CharField(max_length=3)

