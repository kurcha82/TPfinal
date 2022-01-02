from django.shortcuts import render
from django.http import HttpResponse
from Postulantes.forms import *
from Postulantes.models import *
from django.template import loader
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin #Para que solo personas REGISTRADAS, puedan acceder a una clase
from django.contrib.auth.decorators import login_required #DECORADORES
from django.contrib import messages

# Create your views here.


@login_required


def postulantes(request):

    return render(request, 'Postulantes/postulantes.html')


def postFormulario(request):

    #obtiene los datos de nombre y categoria del equipo
    if request.method == "POST":

        miFormulario = PostFormulario(request.POST)

        if miFormulario.is_valid(): #IMPORTANTE LOS PARENTESIS!!!!

            informacion = miFormulario.cleaned_data

            entreInst = Postulante(nombre= informacion["nombre"], apellido= informacion["apellido"], mail = informacion["mail"], telefono = informacion["telefono"], presentacion = informacion["presentacion"], formacion=informacion["formacion"])

            entreInst.save()

            messages.add_message(request=request, level=messages.SUCCESS, message="Postulante cargado con éxito")

            return render(request, 'Login/inicio.html')

    else:

        miFormulario = PostFormulario()


    return render(request, 'Postulantes/postFormulario.html', {"miFormulario":miFormulario})