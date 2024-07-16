from django.shortcuts import render

def signup(request):
    # Define lógica para el registro aquí
    return render(request, 'registration/signup.html')

def login(request):
    # Define lógica para el inicio de sesión aquí
    return render(request, 'registration/login.html')

def profile(request):
    # Define lógica para el perfil aquí
    return render(request, 'registration/profile.html')

