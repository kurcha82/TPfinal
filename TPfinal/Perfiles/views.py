from django.shortcuts import render
from Postulantes.models import Mensaje
from .models import *
from django.views.generic.edit import  CreateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

@login_required
def miPerfil(request):

    if len(Avatar.objects.filter(usuarioA = request.user.id)) != 0 :    #Mira si hay imágenes en Avatar para este ussuario

        dic = {}

        dic["Avatar"] = Avatar.objects.filter(usuarioA = request.user.id).latest("id")  #Filtra los Avatar de este usuario y se queda con el que tiene el id de Avatar de mayor valor

        return render(request, "Perfiles/mi_perfil.html", dic)

    return render(request, "Perfiles/mi_perfil.html")
        
@method_decorator(login_required, name='dispatch')
class AvatarCreacion(CreateView):
    
    model = Avatar
    template_name = "Perfiles/cambiar_foto.html"
    success_url = "/Login/inicio"
    fields = ["imagen"]

    def form_valid(self, form):
        form.instance.usuarioA = self.request.user #Asigna al campo "usuarioA" del modelo Avatar el valor del usuario que está logueado
        return super().form_valid(form)

@login_required
def detalleMensaje(request, valor):

    mensajes = []

    requerido = []

    f = []

    dic = {}

    todos = Mensaje.objects.all()   #Toma todos los mensajes del la base de datos

    for m in todos:

        if m.de_id == request.user.id or m.para_id == request.user.id:  #Se fija si hay mensajes "de" o "para" el usuario logueado (compara estos campos con los dela BD de Mensajes)

            mensajes.append(m)  # Agrega los mensajes para este usuario en una lista

            if requerido.count(m.post.requerido) == 0:  #Filtra los mensajes por el puesto requerido (sería el asunto del mensaje) y si no está en la lista, lo agrega

                requerido.append(m.post.requerido)  # Agrega el valor del puesto requerido a una lista

    if valor == 'a':    # El valor 'a' se envia por url cuando se ingresa en el template "mensajeLista.html"

        dic["requerido"] = requerido    #Solo envia la lista "requeridos" que funciona como asunto del mensaje

        return render(request, "Perfiles/mensajeLista.html", dic)   

    else:   #De recibir cualqueir otro valor por parámetro. El valor enviado equivale a la posición del objeto de la lista "requerido" que se quiere ver (ver html, forloop.counter0)

        r = requerido[int(valor)] #Toma de la lista "requeridos" el valor enviado por parámetro
            
        for m in mensajes:  #Itera sobre los mensajes de este usuario

                if m.post.requerido_id == r.id: #Si en el mensaje el id de la postulación coincide con el id del que se envio por parámetro, lo agrega a una lsta

                    f.append(m)

        dic["mensaje"] = f

        return render(request, "Perfiles/mensajeDetalle.html", dic)
