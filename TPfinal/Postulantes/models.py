from django.db import models

# Create your models here.

class Postulante(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    eail = models.CharField(max_length=40)
    telefono = models.IntegerField(verbose_name = "Teléfono")
    presentacion = models.CharField(max_length=100, verbose_name = "Presentación")
    formacion = models.CharField(max_length=100, verbose_name = "Formación")

    def __str__(self):
        return f"NOMBRE: {self.nombre} - APELLIDO: {self.apellido}"