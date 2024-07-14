from django.shortcuts import render, get_object_or_404
from .models import Blog  # Cambiado a Blog porque parece que es el modelo que estás utilizando

def blog_list(request):
    blogs = Blog.objects.all()
    return render(request, 'pages/blog_list.html', {'blogs': blogs})

def blog_detail(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)
    return render(request, 'pages/blog_detail.html', {'blog': blog})



