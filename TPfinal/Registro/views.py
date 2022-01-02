from django.shortcuts import redirect, render
from .models import *
from .forms import *
from django.contrib import messages

# Create your views here.

def registro(request):

    return render(request, 'Registro/registro.html')


def registroForm(request):

    #obtiene los datos de nombre y categoria del equipo
    if request.method == "POST":

        miRegistro = RegistroForm(request.POST)

        if miRegistro.is_valid(): #IMPORTANTE LOS PARENTESIS!!!!

            informacion = miRegistro.cleaned_data

            usuario = Registro(nombre= informacion["nombre"], apellido= informacion["apellido"], email = informacion["email"], contrasenia = informacion["contrasenia"], confContrasenia = informacion["confContrasenia"])

            usuario.save()

            return render(request, 'Registro/inicio.html')

    else:

        miRegistro = RegistroForm()

    return render(request, 'Registro/registroForm.html', {"miRegistro":miRegistro})


def register(request):
    if request.method == "POST":
        #form = UserCreationForm(request.POST)
        form= UserRegisterform(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']

            form.save()
            #Mensaje de confirmacion
            messages.add_message(request=request, level=messages.SUCCESS, message="Registro exitoso")
            return render(request, "Login/inicio.html")


    else:
        #form= UserCreationForm()
        form= UserRegisterform()

    return render(request, "Registro/register.html", {"form":form})