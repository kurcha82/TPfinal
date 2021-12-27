from django.urls import path
from Requeridos import views


urlpatterns = [

    path(r'^nuevo$', views.RequeridosCreacion.as_view(), name='RequeridosNuevo'),
    path('requeridoslist', views.RequeridosList.as_view(), name='Requeridos'),
    path(r'^(?P<pk>\d+)$', views.RequeridosDetalle.as_view(), name='RequeridosDetalle'),
    path(r'^editarReq/(?P<pk>\d+)$', views.RequeridosUpdate.as_view(), name='RequeridosEditar'),
    path(r'^borrarReq/(?P<pk>\d+)$', views.RequeridosDelete.as_view(), name='RequeridosBorrar'),

]




