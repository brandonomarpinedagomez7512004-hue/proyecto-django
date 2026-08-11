from django.contrib import admin
from .models import Alumnos, Comentario, ComentarioContacto

class MiAdminSite(admin.AdminSite):
    class Media:
        css = {
            'all': ('admin/css/custom_admin.css',)
        }

# Register your models here.
class AdministrarModelo(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('matricula', 'nombre', 'carrera', 'turno', 'created')
    search_fields = ('matricula', 'nombre', 'carrera', 'turno')
    date_hierarchy = 'created'
    list_filter = ('carrera', 'turno', 'created')

    # Esto es lo nuevo que venía en las diapositivas:
    list_display_links = ('matricula', 'nombre')  # Para hacer clic en la matrícula o nombre
    list_per_page = 5  # Paginación de 5 en 5

    def get_readonly_fields(self, request, obj=None):
        # 1. Si el usuario pertenece al grupo 'usuarios'
        if request.user.groups.filter(name='usuarios').exists():
            return ('matricula', 'carrera', 'turno', 'created', 'updated')

        # 2. Si el usuario pertenece al grupo 'Editores_Eliminadores'
        elif request.user.groups.filter(name='Editores_Eliminadores').exists():
            # Bloqueamos matrícula y turno, pero dejamos libres nombre, carrera y fotografía
            return ('matricula', 'turno', 'created', 'updated')

        # 3. Para el superusuario u otros
        else:
            return ('created', 'updated')

    class Media:
        css = {
            'all': ('admin/css/custom_admin.css',)
        }


admin.site.register(Alumnos, AdministrarModelo)


class AdministrarComentarios(admin.ModelAdmin):
    list_display = ('id', 'coment', 'alumno')
    search_fields = ('id', 'created')
    date_hierarchy = 'created'
    readonly_fields = ('created', 'id')
    list_filter = ('alumno', 'created')
    list_display_links = ('id',)

    class Media:
        css = {
            'all': ('admin/css/custom_admin.css',)
        }


admin.site.register(Comentario, AdministrarComentarios)


class AdministrarComentariosContacto(admin.ModelAdmin):
    list_display = ('id', 'mensaje')
    search_fields = ('id', 'created')
    date_hierarchy = 'created'
    readonly_fields = ('created', 'id')

    class Media:
        css = {
            'all': ('admin/css/custom_admin.css',)
        }


admin.site.register(ComentarioContacto, AdministrarComentariosContacto)
