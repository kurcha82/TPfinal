from django.urls import path
from Perfiles import views

urlpatterns = [

    path('miPerfil', views.miPerfil, name='MiPerfil'),
    path(r'^avatarNuevo$', views.AvatarCreacion.as_view(), name='CambiarFoto'),
    path('mensajesLista', views.listaMensajes, name='MensjesLista'),

]