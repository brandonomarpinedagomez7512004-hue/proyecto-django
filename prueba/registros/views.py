from django.shortcuts import render
from .models import Alumnos, ComentarioContacto  # Agregamos ComentarioContacto
from .forms import ComentarioContactoForm  # Importamos el formulario


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