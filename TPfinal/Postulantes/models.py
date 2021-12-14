from django.db import models

# Create your models here.
class Postulante(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    mail = models.CharField(max_length=40)
    telefono = models.IntegerField()
    presentacion = models.CharField(max_length=100)
    formacion = models.CharField(max_length=100)