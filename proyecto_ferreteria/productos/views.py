from django.shortcuts import render

def producto_list(request):
    # Aquí puedes agregar lógica para listar todos los productos si es necesario
    return render(request, "productos/producto_list.html")

