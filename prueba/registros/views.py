from django.shortcuts import render
from .models import Alumnos  # Accedemos al modelo Alumnos
from .forms import ComentarioContactoForm  # Importamos el formulario


# Create your views here.
def registros(request):
    # Recupera todos los objetos/registros de la tabla alumnos
    alumnos = Alumnos.objects.all()

    # Enviamos la lista de alumnos recuperados al template dentro de un diccionario
    return render(request, "registros/principal.html", {'alumnos': alumnos})


def contacto(request):
    return render(request, "registros/contacto.html")
    # Función de visualización del formulario


def registrar(request):
    if request.method == 'POST':
        form = ComentarioContactoForm(request.POST)
        if form.is_valid():  # Si los datos recibidos son correctos
            form.save()  # inserta
            return render(request, 'registros/contacto.html')
    form = ComentarioContactoForm()
    # Si sale mal se reenvían al formulario los datos ingresados
    return render(request, 'registros/contacto.html', {'form': form})