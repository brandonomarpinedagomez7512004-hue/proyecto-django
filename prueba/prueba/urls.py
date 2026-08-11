from django.contrib import admin
from django.urls import path
from inicio import views
from django.conf import settings
from registros import views as views_registros

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views_registros.registros, name="Principal"),
    path('nombre/', views.nombre, name="Nombre"),
    path('contacto/', views_registros.contacto, name="Contacto"),
    path('registrar/', views_registros.registrar, name="Registrar"),
    path('consultarComentario/', views_registros.consultarComentario, name="ConsultarComentario"),
    path('eliminarComentario/<int:id>/', views_registros.eliminarComentarioContacto, name='Eliminar'),
    path('editarComentario/<int:id>/', views_registros.editarComentarioContacto, name='Editar'),
    path('formulario/', views.formulario, name="Formulario"),
    path('ejemplo/', views.ejemplo, name='ejemplo'),
    path('consultas/', views_registros.consultas, name='consultas'),
    path('consultas1', views_registros.consultar1, name="Consultas"),
    path('consultas2', views_registros.consultar2, name="Consultas2"),
    path('consultas3', views_registros.consultar3, name="Consultas3"),
    path('consultas4', views_registros.consultar4, name="Consultas4"),
    path('consultas5', views_registros.consultar5, name="Consultas5"),
    path('consultaComentarios1', views_registros.consultaComentarios1, name="ConsultaComentarios1"),
    path('consultaComentarios2', views_registros.consultaComentarios2, name="ConsultaComentarios2"),
    path('consultaComentarios3', views_registros.consultaComentarios3, name="ConsultaComentarios3"),
    path('consultaComentarios4', views_registros.consultaComentarios4, name="ConsultaComentarios4"),
    path('consultaComentarios5', views_registros.consultaComentarios5, name="ConsultaComentarios5"),
    path('consultaComentariosSQL1', views_registros.consultaComentariosSQL1, name="ConsultaComentariosSQL1"),
    path('consultaComentariosSQL2', views_registros.consultaComentariosSQL2, name="ConsultaComentariosSQL2"),
    path('consultaComentariosSQL3', views_registros.consultaComentariosSQL3, name="ConsultaComentariosSQL3"),
    path('consultaComentariosSQL4', views_registros.consultaComentariosSQL4, name="ConsultaComentariosSQL4"),
    path('consultaComentariosSQL5', views_registros.consultaComentariosSQL5, name="ConsultaComentariosSQL5"),
    path('subir', views_registros.archivos, name="Subir"),
    path('consultas6', views_registros.consultar6, name="Consultas6"),
    path('consultas7', views_registros.consultar7, name="Consultas7"),
    path('seguridad', views_registros.seguridad, name="Seguridad"),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)