from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import *
from .models import *
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import  CreateView, UpdateView, DeleteView
from django.utils.decorators import method_decorator
from Perfiles.models import Avatar

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

def nav(request):

    if len(Avatar.objects.filter(usuarioA = request.user.id)) != 0 :

        dic = {}

        dic["Avatar"] = Avatar.objects.filter(usuarioA = request.user.id).latest("imagen")

        return render(request, "Requeridos/padre.html", dic)

    return render(request, "Requeridos/padre.html")


