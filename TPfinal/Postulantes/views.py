from django.shortcuts import render
from django.http import HttpResponse
from Postulantes.forms import *
from Postulantes.models import *
from django.template import loader
# Create your views here.

def registroForm(request):

    #obtiene los datos de nombre y categoria del equipo
    if request.method == "POST":

        miRegistro = RegistroForm(request.POST)

        if miRegistro.is_valid(): #IMPORTANTE LOS PARENTESIS!!!!

            informacion = miRegistro.cleaned_data

            usuario = Registro(nombre= informacion["nombre"], apellido= informacion["apellido"], email = informacion["email"], contrasenia = informacion["contrasenia"], confContrasenia = informacion["confContrasenia"])

            usuario.save()

            return render(request, 'Postulantes/inicio.html')

    else:

        miRegistro = RegistroForm()


    return render(request, 'Postulantes/registroForm.html', {"miRegistro":miRegistro})

def registro(request):

    return render(request, 'Postulantes/registro.html')

def ingreso(request):

    return render(request, 'Postulantes/ingreso.html')

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