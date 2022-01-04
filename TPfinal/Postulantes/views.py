from django.shortcuts import render

from .forms import *
from .models import *
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import  CreateView, UpdateView, DeleteView
from django.utils.decorators import method_decorator

# Create your views here.
@method_decorator(login_required, name='dispatch')
class PostulanteCreacion(CreateView):
    
    model = Postulante
    template_name = "Postulantes/Postulante_formulario.html"
    success_url = "/Requeridos/requeridoslist"
    fields = ["nombre", "apellido", "mail", "telefono", "presentacion", "formacion"]

    def form_valid(self, form):
        form.instance.requerido = Requeridos.objects.get(pk=self.kwargs['pk'])
        form.instance.usuario = self.request.user
        return super().form_valid(form)
class MisPostulaciones(DetailView):
    
    model = Postulante
    template_name = "Postulantes/mis_postulaciones.html"

class PostulanteDetalle(DetailView):
    
    model = Postulante
    template_name = "Postulantes/Postulante_detalle.html"

class PostulanteUpdate(UpdateView):
    
    model = Postulante
    template_name = "Postulantes/Postulante_formulario.html"
    success_url = "/Perfiles/miPerfil"
    fields = ["nombre", "apellido", "mail", "telefono", "presentacion", "formacion"]

class PostulanteDelete(DeleteView):
    
    model = Postulante
    template_name = "Postulantes/Postulante_borrar.html"
    success_url = "/Perfiles/miPerfil"