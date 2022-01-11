from django.contrib.auth.decorators import login_required
from .forms import *
from .models import *
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import  CreateView, UpdateView, DeleteView
from django.utils.decorators import method_decorator

@method_decorator(login_required, name='dispatch')
class RequeridosCreacion(CreateView):
    
    model = Requeridos
    template_name = "Requeridos/requeridos_formulario.html"
    success_url = "./requeridoslist"
    fields = ["posicion", "sector", "descripcion", "formacionReq", "deLaEmpresa", "propMonetaria", "fechaPublicacion"]

@method_decorator(login_required, name='dispatch')
class RequeridosList(ListView):
    
    model = Requeridos
    template_name = "Requeridos/requeridos_list.html"

@method_decorator(login_required, name='dispatch')
class RequeridosDetalle(DetailView):
    
    model = Requeridos
    template_name = "Requeridos/Requeridos_detalle.html"

@method_decorator(login_required, name='dispatch')
class RequeridosUpdate(UpdateView):
    
    model = Requeridos
    template_name = "Requeridos/Requeridos_formulario.html"
    success_url = "../requeridoslist"
    fields = ["posicion", "sector", "descripcion", "formacionReq", "deLaEmpresa", "propMonetaria", "fechaPublicacion"]

@method_decorator(login_required, name='dispatch')
class RequeridosDelete(DeleteView):
    
    model = Requeridos
    template_name = "Requeridos/Requeridos_borrar.html"
    success_url = "../requeridoslist"



