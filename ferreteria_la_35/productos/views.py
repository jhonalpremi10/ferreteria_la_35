from django.shortcuts import render

def listar_productos(request):
    return render(request, 'productos/listar_productos.html')

def detalle_producto(request, id):
    return render(request, 'productos/detalle_producto.html', {'id': id})

def blog_index(request):
    return render(request, 'productos/blog_index.html')

def blog_detail(request, post_id):
    return render(request, 'productos/blog_detail.html', {'post_id': post_id})


