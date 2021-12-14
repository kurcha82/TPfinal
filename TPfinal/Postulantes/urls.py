from django.urls import path
from Postulantes import views

urlpatterns = [

    path('inicio/', views.inicio, name="Inicio"),
    path('postulantes', views.postulantes, name="Postulantes"),



]