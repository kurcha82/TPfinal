from django.shortcuts import render
from django.http import HttpResponse
from .forms import *
from .models import *
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.

@login_required

def requeridos(request):

    return render(request, 'Requeridos/requeridos.html')


def reqFormulario(request):

    if request.method == "POST":

        miFormulario = ReqFormulario(request.POST)

        if miFormulario.is_valid():

            informacion = miFormulario.cleaned_data

            entreInst = Requeridos(posicion= informacion["posicion"], sector= informacion["sector"], descripcion = informacion["descripcion"],formacionReq = informacion["formacionReq"], deLaEmpresa = informacion["deLaEmpresa"], propMonetaria = informacion["propMonetaria"], fechaPublicacion = informacion["fechaPublicacion"])

            entreInst.save()

            messages.add_message(request=request, level=messages.SUCCESS, message="Puesto cargado con éxito")

            return render(request, 'Login/inicio.html')

    else:

        miFormulario = ReqFormulario()

    return render(request, 'Requeridos/reqFormulario.html', {"miFormulario":miFormulario})