from django.test import TestCase
from django.urls import reverse
from productos.models import Producto, Categoria

class ProductoDetailViewTest(TestCase):

    def test_detalle_producto(self):
        categoria = Categoria.objects.create(nombre="Categoría de prueba")
        producto = Producto.objects.create(
            nombre="Producto de prueba",
            descripcion="Este es un producto de prueba",
            precio=10.00,
            imagen="producto.jpg",
            categoria=categoria
        )
        response = self.client.get(reverse('detalle_producto', args=[producto.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, producto.nombre)
        self.assertContains(response, producto.descripcion)
        self.assertContains(response, producto.precio)
