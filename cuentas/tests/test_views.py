from django.test import TestCase
from django.urls import reverse
from cuentas.models import Usuario

class RegistroUsuarioTest(TestCase):

    def test_registro_usuario(self):
        data = {
            'username': 'usuariodeprueba',
            'email': 'usuariodeprueba@correo.electronico.com',
            'password1': 'contraseña_segura123',
            'password2': 'contraseña_segura123',
        }
        response = self.client.post(reverse('registro'), data)
        self.assertEqual(response.status_code, 302)  # Redirección después del registro
        self.assertTrue(Usuario.objects.filter(username='usuariodeprueba').exists())
