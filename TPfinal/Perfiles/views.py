from django.shortcuts import render
from .models import *
from django.views.generic.edit import  CreateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

@login_required
def miPerfil(request):

    diccionario = {}

    cantidadDeAvatares = 0

    avatar = Avatar.objects.filter(usuarioA = request.user.id)

    if len(avatar) != 0:
        
        for a in avatar:
            cantidadDeAvatares = cantidadDeAvatares + 1
    
    
        diccionario["avatar"] = avatar[cantidadDeAvatares-1].imagen.url

        return render(request, "Perfiles/mi_perfil.html", diccionario)

    else:

        diccionario["avatar"] = 'a'

        return render(request, "Perfiles/mi_perfil.html", diccionario)
        
@method_decorator(login_required, name='dispatch')
class AvatarCreacion(CreateView):
    
    model = Avatar
    template_name = "Perfiles/cambiar_foto.html"
    success_url = "/Login/inicio"
    fields = ["imagen"]

    def form_valid(self, form):
        form.instance.usuarioA = self.request.user
        return super().form_valid(form)


