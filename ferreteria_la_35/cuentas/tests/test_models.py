

from django.test import TestCase
from cuentas.models import Usuario

class UsuarioModelTest(TestCase):
    
    def setUp(self):
        # Configuración inicial para cada prueba
        self.usuario = Usuario.objects.create(
            username='usuario_prueba',
            email='usuario_prueba@example.com',
            first_name='Nombre',
            last_name='Apellido'
        )

    def test_crear_usuario(self):
        # Verificar que el usuario se haya creado correctamente
        self.assertEqual(self.usuario.username, 'usuario_prueba')
        self.assertEqual(self.usuario.email, 'usuario_prueba@example.com')
        self.assertEqual(self.usuario.first_name, 'Nombre')
        self.assertEqual(self.usuario.last_name, 'Apellido')

    def test_actualizar_usuario(self):
        # Modificar y actualizar datos del usuario
        self.usuario.first_name = 'NuevoNombre'
        self.usuario.save()
        self.assertEqual(self.usuario.first_name, 'NuevoNombre')

    def test_eliminar_usuario(self):
        # Eliminar usuario y verificar que no exista
        usuario_id = self.usuario.id
        self.usuario.delete()
        self.assertFalse(Usuario.objects.filter(id=usuario_id).exists())

