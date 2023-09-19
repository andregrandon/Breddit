from django.test import TestCase
from django.contrib.auth import get_user_model

class TestUserCreation(TestCase):

    def test_create_user(self):
        user_model = get_user_model()
        user_data = {
            'email': 'test@example.com',
            'password': 'testpassword',
        }

        user = user_model.objects.create_user(**user_data)

        # Check if the user was created
        self.assertTrue(user_model.objects.filter(email='test@example.com').exists())

        # Check if the user's password is set correctly
        self.assertTrue(user.check_password('testpassword'))

        # Check if the user is active
        self.assertTrue(user.is_active)
