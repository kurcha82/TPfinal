from .forms import *
from .models import *
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import  CreateView, UpdateView, DeleteView

# Create your views here.

class PostulanteCreacion(CreateView):
    
    model = Postulante
    template_name = "Postulantes/Postulante_formulario.html"
    success_url = "./Postulantelist"
    fields = ["nombre", "apellido", "Mail", "telefono", "presentacion", "formacion"]

class PostulanteList(ListView):
    
    model = Postulante
    template_name = "Postulantes/Postulante_list.html"

class PostulanteDetalle(DetailView):
    
    model = Postulante
    template_name = "Postulantes/Postulante_detalle.html"

class PostulanteUpdate(UpdateView):
    
    model = Postulante
    template_name = "Postulantes/Postulante_formulario.html"
    success_url = "../Postulantelist"
    fields = ["nombre", "apellido", "Mail", "telefono", "presentacion", "formacion"]

class PostulanteDelete(DeleteView):
    
    model = Postulante
    template_name = "Postulantes/Postulante_borrar.html"
    success_url = "../Postulantelist"