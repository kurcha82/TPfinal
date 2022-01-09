from django.contrib import messages
from .forms import *
from .models import *
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import  CreateView, UpdateView, DeleteView
from django.utils.decorators import method_decorator

@method_decorator(login_required, name='dispatch')
class PostulanteCreacion(CreateView):
    
    model = Postulante
    template_name = "Postulantes/Postulante_formulario.html"
    success_url = "/Requeridos/requeridoslist"
    fields = ["telefono", "presentacion", "formacion"]

    def form_valid(self, form):
        form.instance.requerido = Requeridos.objects.get(pk=self.kwargs['pk'])
        form.instance.usuario = self.request.user
        form.save()
        return super().form_valid(form)

@method_decorator(login_required, name='dispatch')
class MisPostulaciones(DetailView):
    
    model = Postulante
    template_name = "Postulantes/mis_postulaciones.html"

@method_decorator(login_required, name='dispatch')
class PostulanteDetalle(DetailView):
    
    model = Postulante
    template_name = "Postulantes/Postulante_detalle.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Avatar'] = Avatar.objects.filter(usuarioA = self.request.user).latest("imagen")
        return context

@method_decorator(login_required, name='dispatch')
class PostulanteUpdate(UpdateView):
    
    model = Postulante
    template_name = "Postulantes/Postulante_formulario.html"
    success_url = "/Perfiles/miPerfil"
    fields = ["nombre", "apellido", "mail", "telefono", "presentacion", "formacion"]
@method_decorator(login_required, name='dispatch')
class PostulanteDelete(DeleteView):
    
    model = Postulante
    template_name = "Postulantes/Postulante_borrar.html"
    success_url = "/Perfiles/miPerfil"

@method_decorator(login_required, name='dispatch')
class MensajeCracion(CreateView):
    
    model = Mensaje
    template_name = "Postulantes/mensaje.html"
    success_url = "/Requeridos/requeridoslist"
    fields = ["mensaje"]

    def form_valid(self, form):
        form.instance.usuPostulado = Postulante.objects.get(pk=self.kwargs['pk'])
        form.instance.usuarioM = self.request.user
        form.save()
        return super().form_valid(form)
