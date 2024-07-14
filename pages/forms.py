from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Usuario  # Asegúrate de importar correctamente tu modelo de Usuario

class RegistroForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Usuario  # Reemplaza 'Usuario' con el nombre correcto de tu modelo de Usuario
        fields = ['username', 'email', 'password']  # Los campos que quieres en tu formulario de registro
