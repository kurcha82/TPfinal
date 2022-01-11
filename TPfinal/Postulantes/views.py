from .forms import *
from .models import *
from django.contrib.auth.decorators import login_required
from django.views.generic.detail import DetailView
from django.views.generic.edit import  CreateView, UpdateView, DeleteView
from django.utils.decorators import method_decorator
from Perfiles.models import Avatar

@method_decorator(login_required, name='dispatch')
class PostulanteCreacion(CreateView):
    
    model = Postulante
    template_name = "Postulantes/Postulante_formulario.html"
    success_url = "/Requeridos/requeridoslist"
    fields = ["telefono", "presentacion", "formacion"]

    def form_valid(self, form):
        form.instance.requerido = Requeridos.objects.get(pk=self.kwargs['pk']) #Asigna al campo "requerido" del modelo Postulante el valor enviado por parámetro (en este caso id del puesto requerido)
        form.instance.usuario = self.request.user   #Asigna al campo "usuario" del modelo Postulante el valor del usuario que está logueado
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

    def get_context_data(self, **kwargs):   #Añade al contesto de la vista, en este caso agrega el avata al detalle del postulante
        context = super().get_context_data(**kwargs)
        p = Postulante.objects.get(pk=self.kwargs['pk'])    #Busca al postulante que se envio por parámetro
        if len(Avatar.objects.filter(usuarioA = p.usuario_id)) != 0 :   #Mira si hay imágenes en Avatar para este ussuario
            context['Avatar'] = Avatar.objects.filter(usuarioA = p.usuario_id).latest("id")  #Filtra los Avatar de este usuario y se queda con el que tiene el id de Avatar de mayor valor y lo añade al contexto
        return context

@method_decorator(login_required, name='dispatch')
class PostulanteUpdate(UpdateView):
    
    model = Postulante
    template_name = "Postulantes/Postulante_formulario.html"
    success_url = "/Perfiles/miPerfil"
    fields = ["telefono", "presentacion", "formacion"]
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
        form.instance.de = self.request.user    #Asigna al campo "de" del modelo Mensaje el valor del usuario que está logueado
        form.instance.para = User.objects.get(pk=self.kwargs['pk']) #Asigna al campo "para" del modelo Mensaje el valor enviado por parámetro (en este caso id del "User" del candidato)
        form.instance.post = Postulante.objects.get(pk=self.kwargs['post']) #Asigna al campo "post" del modelo Mensaje el valor enviado por parámetro (en este caso id de la postulación)
        form.save()
        return super().form_valid(form)
