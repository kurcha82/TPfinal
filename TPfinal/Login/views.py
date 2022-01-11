from django import template
from django.shortcuts import render
from django.http import HttpResponse
from Postulantes.forms import *
from Postulantes.models import *
from Login.models import *
from Login.forms import *
from django.template import loader
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin #Para que solo personas REGISTRADAS, puedan acceder a una clase
from django.contrib.auth.decorators import login_required #DECORADORES
from django.contrib import messages
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView


# Create your views here.

def ingreso(request):

    return render(request, 'Login/ingreso.html')


def loginRequest(request):
    if request.method == "POST":

        form = AuthenticationForm(request, data = request.POST)

        if form.is_valid():

            usuario = form.cleaned_data.get("username")
            contra = form.cleaned_data.get("password")

            user = authenticate(username=usuario, password=contra)

            if user is not None:
                login(request, user)

                return render(request, "Login/inicio.html")
            else:
                return render(request, "Login/ingreso.html", {"mensaje": "DATOS INCORRECTOS"})

        else:
            return render(request, "Login/ingreso.html", {"mensaje": "FORMULARIO INCORRECTO"})


    form = AuthenticationForm() #Formulario sin nada para login

    return render(request, "Login/login.html", {"form":form} )


@login_required
def inicio(request):

    return render(request, 'Login/inicio.html')

@login_required
def editarPerfil(request):

    usuario = request.user

    if request.method == 'POST':

        miFormulario = UserEditform(request.POST)

        if miFormulario.is_valid():

            informacion = miFormulario.cleaned_data

            usuario.email = informacion['email']
            usuario.password1 = informacion['password1']
            usuario.password2 = informacion['password2']

            usuario.save()
            
            messages.add_message(request=request, level=messages.SUCCESS, message="Perfil actualizado con éxito")

            return render(request, "Login/inicio.html")

    else:

        miFormulario = UserEditform(initial={'email':usuario.email})

    return render(request, "Login/editarPerfil.html", {"miFormulario":miFormulario, "usuario":usuario})

def about(request):

    return render(request, 'Login/about.html')

# BLOG DE NOVEDADES

class MensajesList(ListView):

    model= MensajesBlog
    template_name = "Login/mensajes_list.html"

class MensajesDetalle(DetailView):

    model = MensajesBlog
    template_name = "Login/mensajes_detalle.html"


class MensajesCreacion(CreateView):
    model = MensajesBlog
    template_name = "Login/mensajes_formulario.html"
    success_url = "/Login/blogs/list"
    fields = ["fecha", "titulo", "mensaje"]

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        form.save()
        return super().form_valid(form)