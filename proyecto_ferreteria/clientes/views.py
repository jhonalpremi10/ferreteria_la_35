from django.shortcuts import render

def cliente_list(request):
    # Define lógica para listar todos los clientes aquí
    return render(request, 'clientes/cliente_list.html')

