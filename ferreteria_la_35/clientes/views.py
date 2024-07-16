from django.shortcuts import render

def cliente_list(request):
    return render(request, 'clientes/cliente_list.html')

def cliente_detail(request, cliente_id):
    return render(request, 'clientes/cliente_detail.html', {'cliente_id': cliente_id})

