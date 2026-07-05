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

    # Nueva ruta para consultar los comentarios directamente
    path('consultarComentario/', views_registros.consultarComentario, name="ConsultarComentario"),

    path('formulario/', views.formulario, name="Formulario"),
    path('ejemplo/', views.ejemplo, name='ejemplo'),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)