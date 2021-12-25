from django.urls import path
from Registro import views

urlpatterns = [

    path('registro/', views.registro, name="Registro"),
    path('registroForm', views.registroForm, name="RegistroForm"),
    path('register', views.register, name="Register"),    

]