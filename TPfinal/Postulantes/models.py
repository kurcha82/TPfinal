from django.contrib.auth.models import User
from django.db import models
from Requeridos.models import Requeridos
# Create your models here.

class Postulante(models.Model):

    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    mail = models.CharField(max_length=40)
    telefono = models.IntegerField(verbose_name = "Teléfono")
    presentacion = models.CharField(max_length=100, verbose_name = "Presentación")
    formacion = models.CharField(max_length=100, verbose_name = "Formación")
    requerido = models.ForeignKey(Requeridos, on_delete=models.CASCADE)

    def __str__(self):
        return f"NOMBRE: {self.nombre} - APELLIDO: {self.apellido}"