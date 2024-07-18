# accounts/views.py

from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login as auth_login
from django.contrib import messages
from .forms import CustomUserCreationForm

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            if user is not None:
                auth_login(request, user)
                messages.success(request, 'Registro exitoso. ¡Bienvenido!')
                return redirect('home')  # Asegúrate de que 'home' esté definido en tus URLs
            else:
                messages.error(request, 'Error al autenticar al usuario.')
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
                return redirect('home')  # Asegúrate de que 'home' esté definido en tus URLs
            else:
                form.add_error(None, 'Nombre de usuario o contraseña inválidos')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})
















