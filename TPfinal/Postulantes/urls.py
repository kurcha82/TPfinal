from django.urls import path
from Postulantes import views


urlpatterns = [

    path(r'^nuevo/(?P<pk>\d+)$', views.PostulanteCreacion.as_view(), name='PostulanteNuevo'),
    path('postulantelist', views.PostulanteList.as_view(), name='Postulante'),
    path(r'^(?P<pk>\d+)$', views.PostulanteDetalle.as_view(), name='PostulanteDetalle'),
    path(r'^editarReq/(?P<pk>\d+)$', views.PostulanteUpdate.as_view(), name='PostulanteEditar'),
    path(r'^borrarReq/(?P<pk>\d+)$', views.PostulanteDelete.as_view(), name='PostulanteBorrar'),

]