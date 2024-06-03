from django import forms
from .models import Autor, Libro, Editorial

class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor
        fields = '_all_'

class LibroForm(forms.ModelForm):
    class Meta:
        model = Libro
        fields = '_all_'

class EditorialForm(forms.ModelForm):
    class Meta:
        model = Editorial
        fields = '_all_'