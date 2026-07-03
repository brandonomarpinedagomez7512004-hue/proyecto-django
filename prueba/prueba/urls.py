from django.contrib import admin
from django.urls import path
from inicio import views
from django.conf import settings
from registros import views as views_registros

urlpatterns = [
    path('admin/', admin.site.urls),

    # CAMBIO DE LA PRÁCTICA: Ahora apunta a views_registros.registros en lugar de views.principal
    path('', views_registros.registros, name="Principal"),

    path('nombre/', views.nombre, name="Nombre"),

    # Cambiado para que use la vista de "registros", que renderiza tu contacto.html con el formulario real
    path('contacto/', views_registros.contacto, name="Contacto"),

    # Nueva ruta que faltaba: procesa el POST y guarda en la base de datos
    path('registrar/', views_registros.registrar, name="Registrar"),

    path('formulario/', views.formulario, name="Formulario"),
    path('ejemplo/', views.ejemplo, name='ejemplo'),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)