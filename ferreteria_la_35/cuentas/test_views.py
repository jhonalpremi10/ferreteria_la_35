
import unittest
from django.test import TestCase
from django.urls import reverse

class TestViews(TestCase):
    def test_login_view(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'cuentas/login.html')

    def test_perfil_view(self):
        response = self.client.get(reverse('perfil'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'cuentas/perfil.html')

if __name__ == "__main__":
    unittest.main()
