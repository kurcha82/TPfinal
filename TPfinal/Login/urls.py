from django.urls import path
from Login import views
from django.contrib.auth.views import LogoutView

urlpatterns = [

    path('inicio/', views.inicio, name="Inicio"),
    path('ingreso', views.ingreso, name="Ingreso"),
    path('login', views.loginRequest, name="Login"),
    path('editarPerfil', views.editarPerfil, name="EditarPerfil"),
    path('about', views.about, name="About"),
    path('logout', LogoutView.as_view (template_name = 'Login/Logout.html'), name="Logout"),

    #BLOG DE NOVEDADES

    path('blogs/list', views.MensajesList.as_view(), name="BlogsList"),
    path(r'^Detalle(?P<pk>\d+)$', views.MensajesDetalle.as_view(), name= 'DetalleMensaje'),
    path('new', views.MensajesCreacion.as_view(), name='New'),


]