from django.urls import path
from Requeridos import views

urlpatterns = [

    path('requeridos', views.requeridos, name="Requeridos"),
    path('reqFormulario', views.reqFormulario, name="ReqFormulario"),

]




