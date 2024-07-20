# pages/views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import Page
from .forms import PageForm

def home(request):
    return render(request, 'pages/home.html')

def page_list(request):
    pages = Page.objects.all()
    return render(request, 'pages/page_list.html', {'pages': pages})

def page_detail(request, page_id):
    page = get_object_or_404(Page, id=page_id)
    return render(request, 'pages/page_detail.html', {'page': page})

def add_news(request):
    if request.method == 'POST':
        form = PageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('page_list')
    else:
        form = PageForm()
    return render(request, 'pages/add_news.html', {'form': form})
















