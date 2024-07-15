from django.shortcuts import render, get_object_or_404
from .models import Cliente

def cliente_list(request):
    clientes = Cliente.objects.all()
    return render(request, 'clientes/cliente_list.html', {'clientes': clientes})

def cliente_detail(request, cliente_id):
    cliente = get_object_or_404(Cliente, id=cliente_id)
    return render(request, 'clientes/cliente_detail.html', {'cliente': cliente})

# Otros views según sea necesario
# def cliente_create(request):
#     Implementación para crear un nuevo cliente

# def cliente_update(request, cliente_id):
#     Implementación para actualizar un cliente existente

# def cliente_delete(request, cliente_id):
#     Implementación para eliminar un cliente existente

