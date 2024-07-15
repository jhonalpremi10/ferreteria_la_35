from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

@login_required
def profile(request):
    # Aquí puedes implementar la lógica del perfil de usuario
    return render(request, 'registration/profile.html')

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirecciona al usuario a la página de inicio de sesión
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

def login(request):
    # Aquí puedes implementar la lógica de inicio de sesión, por ejemplo, usando AuthenticationForm
    return render(request, 'registration/login.html')


