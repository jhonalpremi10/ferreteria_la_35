# proyecto_ferreteria/ferreteria/views.py

from django.http import HttpResponse


def home(request):
    return HttpResponse("¡Bienvenido a Ferretería La 35!")