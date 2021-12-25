from django.shortcuts import render
from django.http import HttpResponse
from Postulantes.forms import *
from Postulantes.models import *
from django.template import loader
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin #Para que solo personas REGISTRADAS, puedan acceder a una clase
from django.contrib.auth.decorators import login_required #DECORADORES

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