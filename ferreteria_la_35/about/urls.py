from django.urls import path
from . import views

urlpatterns = [
    # URL para la página 'about'
    path('', views.about_view, name='about'),
]
