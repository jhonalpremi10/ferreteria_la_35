from django.shortcuts import render

def about(request):
    # Aquí puedes agregar lógica relacionada con la vista "Acerca de"
    return render(request, 'about/about.html')

