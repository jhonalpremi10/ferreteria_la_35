from django.shortcuts import render, get_object_or_404
from .models import Page  # Asegúrate de importar tu modelo Page desde donde esté definido

def blog_index(request):
    pages = Page.objects.all()
    return render(request, 'pages/blog_index.html', {'pages': pages})

def blog_detail(request, page_id):
    page = get_object_or_404(Page, id=page_id)
    return render(request, 'pages/blog_detail.html', {'page': page})


