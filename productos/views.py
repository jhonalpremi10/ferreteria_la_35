
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
