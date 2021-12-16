from django.shortcuts import render
from django.http import HttpResponse
from Postulantes.forms import PostFormulario, ReqFormulario
from Postulantes.models import *
from django.template import loader
# Create your views here.

def login(self):
    nom = "gustavo"

    diccionario = {"nombre": nom}

    plantilla = loader.get_template('login.html')

    documento = plantilla.render(diccionario)

    return HttpResponse(documento)


def registro(self):
    nom = "gustavo"

    diccionario = {"nombre": nom}

    plantilla = loader.get_template('registro.html')

    documento = plantilla.render(diccionario)

    return HttpResponse(documento)


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


def reqFormulario(request):

    if request.method == "POST":

        miFormulario = ReqFormulario(request.POST)

        if miFormulario.is_valid():

            informacion = miFormulario.cleaned_data

            entreInst = Requeridos(posicion= informacion["posicion"], sector= informacion["sector"], descripcion = informacion["descripcion"],formacionReq = informacion["formacionReq"], deLaEmpresa = informacion["deLaEmpresa"], propMonetaria = informacion["propMonetaria"], fechaPublicacion = informacion["fechaPublicacion"])

            entreInst.save()

            return render(request, 'Postulantes/inicio.html')

    else:

        miFormulario = ReqFormulario()


    return render(request, 'Postulantes/reqFormulario.html', {"miFormulario":miFormulario})