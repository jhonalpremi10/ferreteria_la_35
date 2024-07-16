from django.shortcuts import render

def about(request):
    # Define lógica para la página "Acerca de mí" aquí
    return render(request, 'about/about.html')

