import os
import django

# Configura Django para usar la configuración del proyecto
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "proyecto_ferreteria.settings")
django.setup()

from productos.models import Producto

def cargar_productos():
    productos = [
        {
            'nombre': 'Martillo',
            'descripcion': 'Martillo de acero de alta calidad',
            'precio': 15.99,
            'imagen': 'productos/martillo.jpg'  # Ajusta la ruta según la ubicación real de la imagen
        },
        {
            'nombre': 'Taladro',
            'descripcion': 'Taladro eléctrico con múltiples velocidades',
            'precio': 120.00,
            'imagen': 'productos/taladro.jpg'  # Ajusta la ruta según la ubicación real de la imagen
        },
        {
            'nombre': 'Llave Inglesa',
            'descripcion': 'Llave inglesa ajustable para diversas tuercas',
            'precio': 25.50,
            'imagen': 'productos/llave_inglesa.jpg'  # Ajusta la ruta según la ubicación real de la imagen
        },
        {
            'nombre': 'Destornillador',
            'descripcion': 'Set de destornilladores de diferentes tamaños',
            'precio': 10.00,
            'imagen': 'productos/destornillador.jpg'  # Ajusta la ruta según la ubicación real de la imagen
        },
        {
            'nombre': 'Sierra',
            'descripcion': 'Sierra manual para cortes precisos',
            'precio': 30.00,
            'imagen': 'productos/sierra.jpg'  # Ajusta la ruta según la ubicación real de la imagen
        },
    ]

    for prod in productos:
        producto, creado = Producto.objects.get_or_create(
            nombre=prod['nombre'],
            defaults={
                'descripcion': prod['descripcion'],
                'precio': prod['precio'],
                'imagen': prod['imagen'],
            }
        )
        if creado:
            print(f"Producto creado: {producto.nombre}")
        else:
            print(f"Producto ya existía: {producto.nombre}")

if __name__ == "__main__":
    cargar_productos()
