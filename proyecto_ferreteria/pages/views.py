from django.shortcuts import render, get_object_or_404
from .models import Page  # Importa el modelo Page

def home(request):
    return render(request, 'pages/home.html')  # Ajusta 'pages/home.html' según la ruta correcta de tu plantilla de inicio

def page_list(request):
    pages = Page.objects.all()
    return render(request, 'pages/page_list.html', {'pages': pages})

def page_detail(request, page_id):
    page = get_object_or_404(Page, id=page_id)
    return render(request, 'pages/page_detail.html', {'page': page})











