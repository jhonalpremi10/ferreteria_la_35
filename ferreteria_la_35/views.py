from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def signup(request):
    # Tu lógica para la vista signup
    return render(request, 'signup.html')

def login(request):
    # Tu lógica para la vista login
    return render(request, 'login.html')

def profile(request):
    # Tu lógica para la vista profile
    return render(request, 'profile.html')

