from django.urls import path
from Postulantes import views

urlpatterns = [

    path('postulantes', views.postulantes, name="Postulantes"),
    path('postFormulario', views.postFormulario, name="PostFormulario"),

]