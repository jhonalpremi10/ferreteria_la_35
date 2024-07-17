from django.shortcuts import render

def cliente_list(request):
    # Aquí puedes agregar lógica para listar todos los clientes si es necesario
    return render(request, "clientes/cliente_list.html")

