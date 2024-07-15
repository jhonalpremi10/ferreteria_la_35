from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

def signup(request):
    form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

def login(request):
    # Implementa la lógica de inicio de sesión aquí
    return render(request, 'registration/login.html')

def profile(request):
    # Implementa la lógica del perfil de usuario aquí
    return render(request, 'registration/profile.html')


