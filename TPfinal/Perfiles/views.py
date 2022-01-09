from django.shortcuts import render
from Postulantes.models import Mensaje, Postulante
from .models import *
from django.views.generic.edit import  CreateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

@login_required
def miPerfil(request):

    if len(Avatar.objects.filter(usuarioA = request.user.id)) != 0 :

        dic = {}

        dic["Avatar"] = Avatar.objects.filter(usuarioA = request.user.id).latest("imagen")

        return render(request, "Perfiles/mi_perfil.html", dic)

    return render(request, "Perfiles/mi_perfil.html")
        
@method_decorator(login_required, name='dispatch')
class AvatarCreacion(CreateView):
    
    model = Avatar
    template_name = "Perfiles/cambiar_foto.html"
    success_url = "/Login/inicio"
    fields = ["imagen"]

    def form_valid(self, form):
        form.instance.usuarioA = self.request.user
        return super().form_valid(form)

@login_required
def detalleMensaje(request, valor):

    mensajes = []

    requerido = []

    f = []

    dic = {}

    todos = Mensaje.objects.all()

    for m in todos:

        if m.de_id == request.user.id or m.para_id == request.user.id:

            mensajes.append(m)

            if requerido.count(m.post.requerido) == 0:

                requerido.append(m.post.requerido)

    if valor == 'a':

        return render(request, "Perfiles/mensajeLista.html", {"requerido":requerido})

    else:

        r = requerido[int(valor)-1]
            
        for m in mensajes:

                if m.post.requerido_id == r.id:

                    f.append(m)

        dic["mensaje"] = f 

        dic["requerido"] = requerido

        dic["valor"] = valor

        return render(request, "Perfiles/mensajeDetalle.html", dic)


def nav(request):

    if request.user.is_authenticated:

        u = request.user.username

        if len(Avatar.objects.filter(usuarioA = request.user.id)) != 0 :

            avatar = Avatar.objects.filter(usuarioA = request.user.id).latest("imagen")

            return render(request, "Perfiles/mi_perfil.html", {"Avatar":avatar, "usuario": u})

        return render(request, "Requeridos/padre.html", {"usuario": u})
