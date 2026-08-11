from django.shortcuts import render
from .models import Alumnos, ComentarioContacto  # Agregamos ComentarioContacto
from .models import Archivos
from .forms import ComentarioContactoForm  # Importamos el formulario
from .forms import FormArchivos
from django.shortcuts import get_object_or_404
from django.contrib import messages
import datetime




# Create your views here.
def registros(request):
    alumnos = Alumnos.objects.all()
    return render(request, "registros/principal.html", {'alumnos': alumnos})


def contacto(request):
    return render(request, "registros/contacto.html")


def registrar(request):
    if request.method == 'POST':
        form = ComentarioContactoForm(request.POST)
        if form.is_valid():
            form.save()  # inserta
            comentarios = ComentarioContacto.objects.all()
            return render(request, "registros/consultaContacto.html", {'comentarios': comentarios})
    form = ComentarioContactoForm()
    return render(request, 'registros/contacto.html', {'form': form})


def consultarComentario(request):
    # Nueva vista para acceder directamente a la consulta desde el menú
    comentarios = ComentarioContacto.objects.all()
    return render(request, "registros/consultaContacto.html", {'comentarios': comentarios})

def eliminarComentarioContacto(request, id,
    confirmacion='registros/confirmarEliminacion.html'):
    comentario = get_object_or_404(ComentarioContacto, id=id)
    if request.method == 'POST':
        comentario.delete()
        comentarios = ComentarioContacto.objects.all()
        return render(request, "registros/consultaContacto.html",
            {'comentarios': comentarios})
    return render(request, confirmacion, {'object': comentario})

def editarComentarioContacto(request, id):
    return render(request, 'registros/editarComentario.html')

def consultas(request):
    alumnos = Alumnos.objects.all()
    return render(request, "registros/consultas.html", {'alumnos': alumnos})

def consultar1(request):
    # con una sola condición
    alumnos = Alumnos.objects.filter(carrera="TI")
    return render(request, "registros/consultas.html", {'alumnos': alumnos})

def consultar2(request):
    # multiples condiciones adicionando .filter() se analiza
    # como AND
    alumnos = Alumnos.objects.filter(carrera="TI").filter(turno="Matutino")
    return render(request, "registros/consultas.html", {'alumnos': alumnos})

def consultar3(request):
    # Si solo deseamos recuperar ciertos datos agregamos la
    # función only, listando los campos que queremos obtener de
    # la consulta emplear filter() o en el ejemplo all()
    alumnos = Alumnos.objects.all().only("matricula", "nombre", "carrera", "turno", "image")
    return render(request, "registros/consultas.html", {'alumnos': alumnos})

def consultar4(request):
    # __startswith: busca los registros cuyo campo inicia con el valor dado
    alumnos = Alumnos.objects.filter(matricula__startswith="UTM")
    return render(request, "registros/consultas.html", {'alumnos': alumnos})

def consultar5(request):
    # __icontains: como __contains pero no distingue mayúsculas de minúsculas
    alumnos = Alumnos.objects.filter(nombre__icontains="juan")
    return render(request, "registros/consultas.html", {'alumnos': alumnos})

# ---------- Consultas ORM sobre ComentarioContacto ----------

def consultaComentarios1(request):
    # encuentra comentarios creados entre el 8 y 9 de julio 
    fechaInicio = datetime.date(2026, 7, 8) 
    fechaFin = datetime.date(2026, 7, 9) 
    comentarios = ComentarioContacto.objects.filter(created__range=(fechaInicio, fechaFin)) 
    return render(request, "registros/consultasContactos.html", {'comentarios': comentarios})


def consultaComentarios2(request):
    # encuentra  comentarios que contengan una expresión dentro del mensaje
    comentarios = ComentarioContacto.objects.filter(mensaje__icontains="hola")
    return render(request, "registros/consultasContactos.html", {'comentarios': comentarios})


def consultaComentarios3(request):
    # encuentra  comentarios que pertenezcan a un usuario específico
    comentarios = ComentarioContacto.objects.filter(usuario__exact="brandon")
    return render(request, "registros/consultasContactos.html", {'comentarios': comentarios})


def consultaComentarios4(request):
     # Retorna únicamente el campo mensaje de cada comentario (no el objeto completo) 
     comentarios = ComentarioContacto.objects.only('mensaje') 
     return render(request, "registros/consultasContactos.html", {'comentarios': comentarios})


def consultaComentarios5(request):
    # encuentra  comentarios cuyo mensaje termine con cierto texto 
    comentarios = ComentarioContacto.objects.filter(mensaje__endswith="gracias")
    return render(request, "registros/consultasContactos.html", {'comentarios': comentarios})

# ---------- Mismas consultas usando SQL directo (raw) ----------

def consultaComentariosSQL1(request):
    # encuentra comentarios creados entre el 20 de junio y el 4 de agosto
    comentarios = ComentarioContacto.objects.raw(
        'SELECT id, usuario, mensaje, created FROM registros_comentariocontacto '
        'WHERE created BETWEEN "2026-06-20" AND "2026-08-04"'
    )
    return render(request, "registros/consultasContactos.html", {'comentarios': comentarios})


def consultaComentariosSQL2(request):
    # encuentra comentarios que contengan una expresión dentro del mensaje
    comentarios = ComentarioContacto.objects.raw(
        'SELECT id, usuario, mensaje, created FROM registros_comentariocontacto '
        'WHERE mensaje LIKE "%hola%"'
    )
    return render(request, "registros/consultasContactos.html", {'comentarios': comentarios})


def consultaComentariosSQL3(request):
    # encuentra comentarios que pertenezcan a un usuario específico
    comentarios = ComentarioContacto.objects.raw(
        'SELECT id, usuario, mensaje, created FROM registros_comentariocontacto '
        'WHERE usuario = "brandon"'
    )
    return render(request, "registros/consultasContactos.html", {'comentarios': comentarios})


def consultaComentariosSQL4(request):
    # encuentra comentarios cuyo usuario empiece con cierto texto
    comentarios = ComentarioContacto.objects.raw(
        'SELECT id, usuario, mensaje, created FROM registros_comentariocontacto '
        'WHERE usuario LIKE "j%"'
    )
    return render(request, "registros/consultasContactos.html", {'comentarios': comentarios})


def consultaComentariosSQL5(request):
    # encuentra comentarios cuyo mensaje termine con cierto texto
    comentarios = ComentarioContacto.objects.raw(
        'SELECT id, usuario, mensaje, created FROM registros_comentariocontacto '
        'WHERE mensaje LIKE "%gracias"'
    )
    return render(request, "registros/consultasContactos.html", {'comentarios': comentarios})

def archivos(request):
    if request.method == 'POST':
        form = FormArchivos(request.POST, request.FILES)
        if form.is_valid():
            titulo = request.POST['titulo']
            descripcion = request.POST['descripcion']
            archivo = request.FILES['archivo']
            insert = Archivos(titulo=titulo, descripcion=descripcion, archivo=archivo)
            insert.save()
            messages.success(request, "Archivo subido correctamente")
            return render(request, "registros/archivos.html", {'form': FormArchivos()})
        else:
            messages.error(request, "Error al procesar el formulario")
            return render(request, "registros/archivos.html", {'form': form})
    else:
        form = FormArchivos()
    return render(request, "registros/archivos.html", {'form': form})

def consultar6(request):
    # __range: búsqueda por rango de fechas usando el campo 'created'
    fechaInicio = datetime.date(2026, 1, 1)
    fechaFin = datetime.date(2026, 12, 31)
    
    alumnos = Alumnos.objects.filter(created__range=(fechaInicio, fechaFin))
    
    return render(request, "registros/consultas.html", {'alumnos': alumnos})

def consultar7(request):
    # Consulta entre modelos: alumnos que tengan un comentario con cierto texto
    alumnos = Alumnos.objects.filter(comentario__coment__icontains='inscrito')
    
    return render(request, "registros/consultas.html", {'alumnos': alumnos})

def seguridad(request):
    nombre = request.GET.get('nombre')
    return render(
        request,
        "registros/seguridad.html",
        {'nombre': nombre}
    )
