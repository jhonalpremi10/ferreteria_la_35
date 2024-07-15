from django.shortcuts import render
from .models import Producto  # Asegúrate de importar el modelo Producto adecuadamente

def listar_productos(request):
    productos = Producto.objects.all()
    return render(request, 'productos/producto_list.html', {'productos': productos})

def detalle_producto(request, id):
    producto = Producto.objects.get(id=id)  # O usa get_object_or_404 para manejar casos donde el producto no existe
    return render(request, 'productos/producto_detail.html', {'producto': producto})

def blog_index(request):
    # Aquí puedes definir la lógica para mostrar un índice de tu blog de productos
    return render(request, 'productos/blog_index.html')

def blog_detail(request, post_id):
    # Aquí puedes definir la lógica para mostrar detalles de un post específico de tu blog de productos
    return render(request, 'productos/blog_detail.html')

