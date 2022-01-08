from django.shortcuts import render
from django.http import HttpResponse
from Postulantes.forms import *
from Postulantes.models import *
from Login.forms import *
from django.template import loader
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin #Para que solo personas REGISTRADAS, puedan acceder a una clase
from django.contrib.auth.decorators import login_required #DECORADORES
from django.contrib import messages
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