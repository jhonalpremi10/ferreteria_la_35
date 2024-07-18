from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login as auth_login
from .forms import CustomUserCreationForm
from django.contrib import messages  # Importa el módulo de mensajes

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Registro exitoso. Ahora puedes iniciar sesión.")
            return redirect('home')  # Redirige a la página de inicio
        else:
            messages.error(request, "Formulario inválido. Por favor, revisa los datos ingresados.")
    else:
        form = CustomUserCreationForm()
    return render(request, 'accounts/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect('home')  # Redirige a la página de inicio
            else:
                form.add_error(None, 'Usuario o contraseña incorrectos.')
        else:
            messages.error(request, "Formulario inválido. Por favor, revisa los datos ingresados.")
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})

def profile(request):
    # Implementa la lógica del perfil aquí
    pass








