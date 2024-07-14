from django.shortcuts import render
from .models import Blog, Producto
  
 


def blog_list(request):
    blogs = Blog.objects.all()
    return render(request, 'pages/blog_list.html', {'blogs': blogs})

def blog_detail(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)
    return render(request, 'pages/blog_detail.html', {'blog': blog})

def listar_productos(request):
    productos = Producto.objects.all()  
    return render(request, 'pages/listar_productos.html', {'productos': productos})






