from django.urls import path
from . import views

urlpatterns = [
    path("", views.cliente_list, name="cliente_list"),
    # Puedes definir más URLs según sea necesario para clientes
]

