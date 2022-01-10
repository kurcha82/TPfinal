from django.urls import path
from Perfiles import views

urlpatterns = [

    path('miPerfil', views.miPerfil, name='MiPerfil'),
    path('cambiarFoto', views.AvatarCreacion.as_view(), name='CambiarFoto'),
    path(r'^ListaeM(?P<valor>\d+)$', views.detalleMensaje, name='MensjesLista'),
    path(r'^DetalleM(?P<valor>\d+)$', views.detalleMensaje, name='MensjesDetalle'),
    

]