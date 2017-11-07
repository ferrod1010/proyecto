from django.conf.urls import url
from . import views


urlpatterns = [

    url(r'^vehiculo/nuevo/$', views.vehiculo_nuevo, name='vehiculo_nuevo'),
    url(r'^vehiculos', views.vehiculo_lista, name = 'vehiculo_lista'),
    url(r'^vehiculo/(?P<pk>[0-9]+)/$', views.vehiculo_detalle, name='vehiculo_detalle'),
    url(r'^vehiculo/nuevo/$', views.vehiculo_nuevo, name='vehiculo_nuevo'),
    url(r'^vehiculo/(?P<pk>[0-9]+)/editar/$', views.vehiculo_editar, name='vehiculo_editar'),
    url(r'^vehiculo/(?P<pk>\d+)/del/$', views.vehiculo_del, name='vehiculo_del'),
    url(r'^repuestos/', views.repuesto_lista, name='repuesto_lista'),
    url(r'^repuesto/(?P<pk>[0-9]+)/$', views.repuesto_detalle, name='repuesto_detalle'),
    url(r'^repuesto/nuevo/$', views.repuesto_nuevo, name='repuesto_nuevo'),
    url(r'^repuesto/(?P<pk>[0-9]+)/editar/$', views.repuesto_editar, name='repuesto_editar'),
    url(r'^repuesto/(?P<pk>\d+)/del/$', views.repuesto_del, name='repuesto_del'),
    url(r'^$', views.asignacion_lista, name='asignacion_lista'),
    url(r'^asignacion/(?P<pk>[0-9]+)/$', views.asignacion_detalle, name='asignacion_detalle'),
    url(r'^asignacion/nueva/$', views.asignacion_nueva, name='asignacion_nueva'),
    url(r'^asignacion/(?P<pk>[0-9]+)/editar/$', views.asignacion_editar, name='asignacion_editar'),
    url(r'^asignacion/(?P<pk>\d+)/del/$', views.asignacion_del, name='asignacion_del'),
    ]
