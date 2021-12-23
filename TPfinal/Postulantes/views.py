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

    return render(request, 'Postulantes/ingreso.html')


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


@login_required
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

def loginRequest(request):
    if request.method == "POST":

        form = AuthenticationForm(request, data = request.POST)

        if form.is_valid():

            usuario = form.cleaned_data.get("username")
            contra = form.cleaned_data.get("password")

            user = authenticate(username=usuario, password=contra)

            if user is not None:
                login(request, user)

                return render(request, "Postulantes/inicio.html")
            else:
                return render(request, "Postulantes/ingreso.html", {"mensaje": "DATOS INCORRECTOS"})

        else:
            return render(request, "Postulantes/ingreso.html", {"mensaje": "FORMULARIO INCORRECTO"})


    form = AuthenticationForm() #Formulario sin nada para login

    return render(request, "Postulantes/login.html", {"form":form} )

def register(request):
    if request.method == "POST":
        #form = UserCreationForm(request.POST)
        form= UserRegisterform(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']

            form.save()

            return render(request, "Postulantes/inicio.html")

    else:
        #form= UserCreationForm()
        form= UserRegisterform()

    return render(request, "Postulantes/register.html", {"form":form})