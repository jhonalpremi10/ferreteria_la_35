from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'cuentas/signup.html', {'form': form})

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('profile')
    else:
        form = AuthenticationForm()
    return render(request, 'cuentas/login.html', {'form': form})

def profile(request):
    return render(request, 'cuentas/profile.html')


