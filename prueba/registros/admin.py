from django.contrib import admin
from .models import Alumnos, Comentario, ComentarioContacto

# Register your models here.
class AdministrarModelo(admin.ModelAdmin):
    readonly_fields = ('created', 'updatep') 
    list_display = ('matricula', 'nombre', 'carrera','turno')
    search_fields = ('matricula','nombre','carrera','turno')
    date_hierarchy = 'created'
    list_filter = ('carrera','turno')

admin.site.register(Alumnos, AdministrarModelo)

class AdministrarComentarios(admin.ModelAdmin):
    list_display = ('id', 'coment', 'alumno')  # ← agrega 'alumno' aquí
    search_fields = ('id', 'created')  
    date_hierarchy = 'created'           # ← sin paréntesis
    readonly_fields = ('created', 'id') 
    list_filter = ('alumno', 'created')
    list_display_links = ('id',)         # ← enlaza 'id' que sí está en list_display
   

admin.site.register(Comentario, AdministrarComentarios)


class AdministrarComentariosContacto(admin.ModelAdmin):
    list_display = ('id', 'mensaje')
    search_fields = ('id', 'created')
    date_hierarchy = 'created'
    readonly_fields = ('created', 'id')

admin.site.register(ComentarioContacto, AdministrarComentariosContacto)