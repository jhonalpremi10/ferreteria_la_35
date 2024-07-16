<<<<<<< HEAD
from django.shortcuts import render

def listar_productos(request):
    return render(request, 'productos/listar_productos.html')

def detalle_producto(request, id):
    return render(request, 'productos/detalle_producto.html', {'id': id})

def blog_index(request):
    return render(request, 'productos/blog_index.html')

def blog_detail(request, post_id):
    return render(request, 'productos/blog_detail.html', {'post_id': post_id})


=======

from django.shortcuts import render, get_object_or_404
from .models import Producto, Post
from .forms import ProductoForm

# Vista para listar productos
def listar_productos(request):
    productos = Producto.objects.all()
    return render(request, 'productos/listar_productos.html', {'productos': productos})

# Vista para el detalle del producto
def detalle_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    return render(request, 'productos/detalle_producto.html', {'producto': producto})

# Vista para listar posts del blog
def blog_index(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'productos/blog_index.html', {'posts': posts})

# Vista para el detalle del post
def blog_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, 'productos/blog_detail.html', {'post': post})
>>>>>>> b9b18d95c12427cd9661ca7a32aeae6a5b2e9c31
