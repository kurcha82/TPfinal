from django.urls import path
from Postulantes import views


urlpatterns = [

    path(r'^nuevo/(?P<pk>\d+)$', views.PostulanteCreacion.as_view(), name='PostulanteNuevo'),
    path(r'^(?P<pk>\d+)$', views.MisPostulaciones.as_view(),name='MisPostulaciones'),
    path(r'^Detalle(?P<pk>\d+)$', views.PostulanteDetalle.as_view(), name='PostulanteDetalle'),
    path(r'^editarReq/(?P<pk>\d+)$', views.PostulanteUpdate.as_view(), name='PostulanteEditar'),
    path(r'^borrarReq/(?P<pk>\d+)$', views.PostulanteDelete.as_view(), name='PostulanteBorrar'),
    path(r'^mensaje/(?P<pk>\d+)/(?P<post>\d+)/$', views.MensajeCracion.as_view(), name='Mensaje'),

]