from django.shortcuts import render
from .models import *
from .forms import *
from django.contrib import messages

# Create your views here.

def registro(request):

    return render(request, 'Registro/registro.html')

def register(request):
    if request.method == "POST":
        #form = UserCreationForm(request.POST)
        form= UserRegisterform(request.POST)
        if form.is_valid():

            form.save()
            #Mensaje de confirmacion
            messages.add_message(request=request, level=messages.SUCCESS, message="Registro exitoso")
            return render(request, "Login/inicio.html")


    else:
        #form= UserCreationForm()
        form= UserRegisterform()

    return render(request, "Registro/register.html", {"form":form})