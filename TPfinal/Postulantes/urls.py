from django.urls import path
from Postulantes import views

urlpatterns = [

    path('inicio/', views.inicio, name="Inicio"),
    path('postulantes', views.postulantes, name="Postulantes"),
    path('requeridos', views.requeridos, name="Requeridos"),
    path('postFormulario', views.postFormulario, name="PostFormulario"),
    path('reqFormulario', views.reqFormulario, name="ReqFormulario"),
    #path('login', views.login, name="Login"),
    path('registro', views.registro, name="Registro"),
    path('registroForm', views.registroForm, name="RegistroForm"),
    path('ingreso', views.ingreso, name="Ingreso")

]