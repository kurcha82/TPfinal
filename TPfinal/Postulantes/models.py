from django.contrib.auth.models import User
from django.db import models
from Perfiles.models import Avatar
from Requeridos.models import Requeridos
# Create your models here.

class Postulante(models.Model):

    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    telefono = models.IntegerField(verbose_name = "Teléfono")
    presentacion = models.CharField(max_length=300, verbose_name = "Presentación")
    formacion = models.CharField(max_length=300, verbose_name = "Formación")
    requerido = models.ForeignKey(Requeridos, on_delete=models.CASCADE)

class Mensaje(models.Model):
    de  = models.ForeignKey(User, on_delete=models.CASCADE)
    para = models.ForeignKey(User, on_delete=models.CASCADE, related_name="para")
    post = models.ForeignKey(Postulante, on_delete=models.CASCADE)
    mensaje = models.TextField(max_length=300)