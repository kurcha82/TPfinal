from django.urls import path
from Login import views

urlpatterns = [

    path('inicio/', views.inicio, name="Inicio"),
    path('ingreso', views.ingreso, name="Ingreso"),
    path('login', views.loginRequest, name="Login"),
    path('editarPerfil', views.editarPerfil, name="EditarPerfil"),
    path('about', views.about, name="About"),

]