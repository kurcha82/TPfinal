from django.shortcuts import render
from django.http import HttpResponse
from Postulantes.forms import PostFormulario
from Postulantes.models import *

# Create your views here.
def inicio(request):

    return render(request, 'Postulantes/inicio.html')

def postulantes(request):

    return render(request, 'Postulantes/postulantes.html')

def requeridos(request):

    return render(request, 'Postulantes/requeridos.html')

def postFormulario(request):

    #obtiene los datos de nombre y categoria del equipo
    if request.method == "POST":

        miFormulario = PostFormulario(request.POST)

        if miFormulario.is_valid(): #IMPORTANTE LOS PARENTESIS!!!!

            informacion = miFormulario.cleaned_data

            entreInst = Postulante(nombre= informacion["nombre"], apellido= informacion["apellido"], mail = informacion["mail"], telefono = informacion["telefono"], presentacion = informacion["presentacion"], formacion=informacion["formacion"])

            entreInst.save()

            return render(request, 'Postulantes/inicio.html')

    else:

        miFormulario = PostFormulario()


    return render(request, 'Postulantes/postFormulario.html', {"miFormulario":miFormulario})