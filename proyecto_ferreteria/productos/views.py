from django.shortcuts import render

def producto_list(request):
    # Define lógica para listar todos los productos aquí
    return render(request, 'productos/producto_list.html')

