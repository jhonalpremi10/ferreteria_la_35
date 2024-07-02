
from django.shortcuts import render, redirect
from .forms import EstudianteForm, ProfesorForm, CursoForm, ActividadExtracurricularForm

def insertar_datos(request):
    if request.method == 'POST':
        estudiante_form = EstudianteForm(request.POST)
        profesor_form = ProfesorForm(request.POST)
        curso_form = CursoForm(request.POST)
        actividad_form = ActividadExtracurricularForm(request.POST)
        if (estudiante_form.is_valid() and 
            profesor_form.is_valid() and 
            curso_form.is_valid() and 
            actividad_form.is_valid()):
            estudiante = estudiante_form.save()
            profesor = profesor_form.save()
            curso = curso_form.save()
            actividad = actividad_form.save()
            return redirect('ruta_hacia_donde_redirigir_después_de_insertar')
    else:
        estudiante_form = EstudianteForm()
        profesor_form = ProfesorForm()
        curso_form = CursoForm()
        actividad_form = ActividadExtracurricularForm()
    return render(request, 'insertar_datos.html', {'estudiante_form': estudiante_form, 
                                                    'profesor_form': profesor_form, 
                                                    'curso_form': curso_form, 
                                                    'actividad_form': actividad_form})
