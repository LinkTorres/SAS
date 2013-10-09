from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
admin.autodiscover()

urlpatterns = patterns('',


	url(r'^$','principal.views.inicio', name='inicio'),
	url(r'^profesor_main/$','principal.views.profesor_main'),
	url(r'^profesor_preferencias/$','principal.views.profesor_preferencias'),
	url(r'^profesor_logout/$','principal.views.profesor_logout'),
    url(r'^profesor_mis_grupos/$','principal.views.profesor_mis_grupos'),

	url(r'^profesor_registrar_calificaciones/$','principal.views.profesor_registrar_calificaciones'),
	url(r'^directorio/$','principal.views.directorio'),
	url(r'^profesor_reportes_PRUI08_1/$','principal.views.profesor_reportes_PRUI08_1'),
	url(r'^profesor_reportes_PRUI08_2/$','principal.views.profesor_reportes_PRUI08_2'),
	url(r'^profesor_calendario/$','principal.views.profesor_calendario'),
	url(r'^profesor_tutorias/$','principal.views.profesor_tutorias'),
	url(r'^profesor_ingresa_calificacion/$','principal.views.profesor_ingresa_calificacion'),
	url(r'^profesor_ingresa_calificacion_extra/$','principal.views.profesor_ingresa_calificacion_extra'),
	url(r'^profesor_ingresa_calificacion_ets/$','principal.views.profesor_ingresa_calificacion_ets'),
	url(r'^perfiles_profesor/$','principal.views.perfiles_profesor'),
	url(r'^perfiles_materia/$','principal.views.perfiles_materia'),
	url(r'^perfiles_grupo/$','principal.views.perfiles_grupo'),
	url(r'^profesor_tutorias_comentar/$','principal.views.profesor_tutorias_comentar'),
	url(r'^profesor_guarda_calificacion/$','principal.views.profesor_guarda_calificacion'),
	
	url(r'^profesor_miperfil2/$','principal.views.profesor_miperfil2'),
	url(r'^profesor_miperfil/$','principal.views.profesor_miperfil'),
	url(r'^guarda_miperfil/$','principal.views.guarda_miperfil'),
	url(r'^guardar_preferencias/$','principal.views.guardar_preferencias'),

	url(r'^profesor_guarda_calificacionExtra/$','principal.views.profesor_guarda_calificacionExtra'),
	url(r'^profesor_guarda_calificacionETS/$','principal.views.profesor_guarda_calificacionETS'),
	url(r'^profesor_registrar_calificaciones_extra/$','principal.views.profesor_registrar_calificaciones_extra'),
	url(r'^profesor_registrar_calificaciones_ets/$','principal.views.profesor_registrar_calificaciones_ets'),
	url(r'^guardar_comentarios/$','principal.views.guardar_comentarios'),
	url(r'^cerrar/$', 'principal.views.cerrar'),
	url(r'^pdf/$', 'principal.views.pdf'),
	url(r'^profesor_agregar_tutorado/$','principal.views.profesor_agregar_tutorado'),
	url(r'^profesor_tutorias_add/$','principal.views.profesor_tutorias_add'),
	url(r'^recuperar_contrasena/$','principal.views.recuperar_contrasena'),
	url(r'^reporte_lista/$', 'principal.views.reporte_lista'),
	url(r'^reporte_evaluaciones/$', 'principal.views.reporte_evaluaciones'),

	url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
	url(r'^admin/', include(admin.site.urls)),
	url(r'media/(?P<path>.*)', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
  	url(r'static/(?P<path>.*)', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
)


#http://127.0.0.1:8000/media/recetas/