from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
import datetime

# Create your models here.


class MensajesBlog(models.Model):
    usuario = models.ForeignKey(User, on_delete=CASCADE)
    fecha = models.DateField(default = datetime.date.today(),verbose_name = "Fecha de publicación")
    titulo = models.CharField(max_length=100)
    mensaje = models.TextField(max_length=240)

    def __str__(self):
        return f"USUARIO: {self.usuario} - FECHA: {self.fecha} - TITULO: {self.titulo} - MENSAJE: {self.mensaje}"
    
