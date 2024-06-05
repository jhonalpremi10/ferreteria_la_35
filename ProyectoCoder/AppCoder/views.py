

from django.shortcuts import render
from django.http import HttpResponse
from .models import Estudiantes, Profesor, Entregable, Curso
from .forms import CursoFormulario

def inicio(request):
    return render(request, 'AppCoder/inicio.html')

def cursoFormulario(request):
    if request.method == "POST":
        miFormulario = CursoFormulario(request.POST)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            curso = Curso(nombre=informacion["nombre"], comision=informacion["comision"])
            curso.save()
            return render(request, "AppCoder/inicio.html")
    else:
        miFormulario = CursoFormulario()
    return render(request, "AppCoder/cursoFormulario.html", {"miFormulario": miFormulario})

def busquedaCamada(request):
    return render(request, "AppCoder/busquedaCamada.html")

def buscar(request):
    if request.GET["camada"]:
        camada = request.GET["camada"]
        cursos = Curso.objects.filter(comision__icontains=camada)
        return render(request, "AppCoder/resultadosPorBusqueda.html", {"cursos": cursos, "camada": camada})
    else:
        respuesta = "No enviaste datos"
    return HttpResponse(respuesta)

