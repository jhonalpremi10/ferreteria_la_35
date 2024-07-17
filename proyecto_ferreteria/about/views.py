from django.shortcuts import render

def about(request):
    # Aquí puedes agregar lógica adicional si es necesario
    return render(request, "about/about.html")
