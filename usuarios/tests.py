from django.test import TestCase
from django.contrib.auth import get_user_model


class CustomUserTest(TestCase):
    def test_crear_usuario(self):
        Usr = get_user_model()
        usr = Usr.objects.create_user(
            username="unitester", email="unitester@mail.com", password="123"
        )
        # QUÉ ESPERAMOS
        self.assertEqual(usr.username, "unitester")
        self.assertEqual(usr.email, "unitester@mail.com")
        self.assertTrue(usr.is_active)
        self.assertFalse(usr.is_staff)
        self.assertFalse(usr.is_superuser)

    def test_crear_superusuario(self):
        Usr = get_user_model()
        usr = Usr.objects.create_superuser(
            username="unitester", email="unitester@mail.com", password="123"
        )
        # QUÉ ESPERAMOS
        self.assertEqual(usr.username, "unitester")
        self.assertEqual(usr.email, "unitester@mail.com")
        self.assertTrue(usr.is_active)
        self.assertTrue(usr.is_staff)
        self.assertTrue(usr.is_superuser)
