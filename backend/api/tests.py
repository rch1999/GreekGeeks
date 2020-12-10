from django.test import TestCase
from rest_framework.test import APIClient
import api.models as models


class ApiTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_successful_then_duplicate(self):
        data = {
            'first_name': 'Tim',
            'last_name': 'Clough',
            'email': 'tim@example.com',
            'password': 'hunter2'
        }

        # Should succeed
        response = self.client.post('/api/users/', data)
        response_body = response.data

        self.assertTrue('success' in response_body)
        self.assertEquals(response_body['success'], True)

        self.assertTrue('uuid' in response_body)
        self.assertFalse('errorMessage' in response_body)

    def test_add_duplicate(self):
        models.User.objects.create(
            first_name='Tim',
            last_name='Clough',
            email='tim@example.com',
            password='hunter2'
        )

        data = {
            'first_name': 'Tim',
            'last_name': 'Clough',
            'email': 'tim@example.com',
            'password': 'hunter2'
        }

        # Should fail
        response = self.client.post('/api/users/', data)
        response_body = response.data

        self.assertTrue('success' in response_body)
        self.assertEquals(response_body['success'], False)

        self.assertFalse('uuid' in response_body)
        self.assertTrue('errorMessage' in response_body)
