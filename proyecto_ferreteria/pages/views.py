from django.shortcuts import render

def page_list(request):
    # Define lógica para listar todas las páginas aquí
    return render(request, 'pages/page_list.html')

def page_detail(request, page_id):
    # Define lógica para ver detalles de una página específica aquí
    return render(request, 'pages/page_detail.html')

