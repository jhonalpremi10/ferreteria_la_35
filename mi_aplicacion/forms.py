from django import forms
from .models import Estudiante, Profesor, Curso, ActividadExtracurricular

class EstudianteForm(forms.ModelForm):
    class Meta:
        model = Estudiante
        fields = '_all_'

class ProfesorForm(forms.ModelForm):
    class Meta:
        model = Profesor
        fields = '_all_'

class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = '_all_'

class ActividadExtracurricularForm(forms.ModelForm):
    class Meta:
        model = ActividadExtracurricular
        fields = '_all_'
    