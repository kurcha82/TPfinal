from django.db import models
import datetime

# Create your models here.
class Requeridos(models.Model):
    posicion = models.CharField(max_length=40, verbose_name = "Posición")
    sector = models.CharField(max_length=40)
    descripcion = models.CharField(max_length=400, verbose_name = "Descripción")
    formacionReq = models.CharField(max_length=40, verbose_name = "Formación requerida")
    deLaEmpresa = models.BooleanField(null=True, verbose_name = "Interno de la empresa")
    propMonetaria = models.IntegerField(verbose_name = "Propuesta monetaria")
    fechaPublicacion = models.DateField(default = datetime.date.today(),verbose_name = "Fecha de publicación")
    
    def __str__(self):
        return f"POSICIÓN: {self.posicion} - FORMACIÓN: {self.formacionReq} - REQUIERE SER INTERNO: {self.deLaEmpresa}"