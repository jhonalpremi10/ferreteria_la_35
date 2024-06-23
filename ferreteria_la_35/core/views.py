from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("¡Hola, mundo! Esta es la página de inicio.")

def about(request):
    return render(request, 'about.html')  # Asegúrate de tener esta plantilla

