from django.urls import path
from Registro import views

urlpatterns = [

    path('register', views.register, name="Register"),    

]