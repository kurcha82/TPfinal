from django.shortcuts import render
from django.http import HttpResponse
from Postulantes.models import *

# Create your views here.
def inicio(request):

    return render(request, 'Postulantes/inicio.html')

def postulantes(request):

    return render(request, 'Postulantes/postulantes.html')