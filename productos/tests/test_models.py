from django.test import TestCase
from productos.models import Producto, Categoria

class ProductoModelTest(TestCase):

    def test_crear_producto(self):
        categoria = Categoria.objects.create(nombre="Categoría de prueba")
        producto = Producto.objects.create(
            nombre="Producto de prueba",
            descripcion="Este es un producto de prueba",
            precio=10.00,
            imagen="producto.jpg",
            categoria=categoria
        )
        self.assertEqual(producto.nombre, "Producto de prueba")
        self.assertEqual(producto.descripcion, "Este es un producto de prueba")
        self.assertEqual(producto.precio, 10.00)
        self.assertEqual(producto.imagen, "producto.jpg")
        self.assertEqual(producto.categoria.nombre, "Categoría de prueba")

    def test_actualizar_producto(self):
        categoria = Categoria.objects.create(nombre="Categoría de prueba")
        producto = Producto.objects.create(
            nombre="Producto de prueba",
            descripcion="Este es un producto de prueba",
            precio=10.00,
            imagen="producto.jpg",
            categoria=categoria
        )
        producto.nombre = "Producto actualizado"
     

