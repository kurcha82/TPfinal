from django.db import models

# Create your models here.

class Registro(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    email = models.CharField(max_length=40)
    contrasenia = models.CharField(max_length=40)
    confContrasenia = models.CharField(max_length=40)

    def __str__(self):
        return f"NOMBRE: {self.nombre} - APELLIDO: {self.apellido}"