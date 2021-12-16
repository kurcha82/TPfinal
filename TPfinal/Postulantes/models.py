from django.db import models

# Create your models here.
class Postulante(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    mail = models.CharField(max_length=40)
    telefono = models.IntegerField()
    presentacion = models.CharField(max_length=100)
    formacion = models.CharField(max_length=100)

    def __str__(self):
        return f"NOMBRE: {self.nombre} - APELLIDO: {self.apellido}"


class Requeridos(models.Model):
    posicion = models.CharField(max_length=40)
    sector = models.CharField(max_length=40)
    descripcion = models.CharField(max_length=400)
    formacionReq = models.CharField(max_length=40)
    deLaEmpresa = models.BooleanField(null=True)
    propMonetaria = models.IntegerField()
    fechaPublicacion = models.DateField()
    
    def __str__(self):
        return f"POSICIÓN: {self.posicion} - FORMACIÓN: {self.formacionReq} - REQUIERE SER INTERNO: {self.deLaEmpresa}"