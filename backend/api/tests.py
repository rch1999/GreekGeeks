from django.test import TestCase, TransactionTestCase
from django.contrib.auth.hashers import check_password
from rest_framework.test import APIClient
from rest_framework import status
import api.models as models


class TokenTestCase(TransactionTestCase):
    def setUp(self):
        self.client = APIClient()
        models.User.objects.create_user(
            first_name='Tim',
            last_name='Clough',
            email='tim@example.com',
            password='hunter2'
        )

    def test_token_valid_credentials(self):
        data = {
            'email': 'tim@example.com',
            'password': 'hunter2'
        }

        response = self.client.post('/api/token/', data)
        self.assertEquals(response.status_code, status.HTTP_200_OK)

        response_body = response.data

        self.assertTrue('access' in response_body)
        self.assertTrue('refresh' in response_body)

    def test_token_invalid_credentials(self):
        data = {
            'email': 'tim2@example.com',
            'password': 'hunter2'
        }

        response = self.client.post('/api/token/', data)
        self.assertEquals(response.status_code, status.HTTP_401_UNAUTHORIZED)

        response_body = response.data

        self.assertTrue('access' not in response_body)
        self.assertTrue('refresh' not in response_body)


class CreateUserTestCase(TransactionTestCase):
    def setUp(self):
        self.client = APIClient()
        models.User.objects.create_user(
            first_name='Tim',
            last_name='Clough',
            email='tim@example.com',
            password='hunter2'
        )

    def test_add_user_successful(self):
        data = {
            'first_name': 'Tim',
            'last_name': 'Clough',
            'email': 'tim2@example.com',
            'password': 'hunter2'
        }

        # Should succeed
        response = self.client.post('/api/users/', data)
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)

        response_body = response.data

        self.assertTrue('success' in response_body)
        self.assertEquals(response_body['success'], True)

        self.assertTrue('uuid' in response_body)
        self.assertFalse('errorMessage' in response_body)

        # Test User exists
        self.assertEquals(models.User.objects
                          .filter(email='tim2@example.com')
                          .count(),
                          1)

    def test_add_user_duplicate(self):
        data = {
            'first_name': 'Tim',
            'last_name': 'Clough',
            'email': 'tim@example.com',
            'password': 'hunter2'
        }

        # Should fail
        response = self.client.post('/api/users/', data)
        self.assertEquals(response.status_code, status.HTTP_400_BAD_REQUEST)

        response_body = response.data

        self.assertTrue('success' in response_body)
        self.assertEquals(response_body['success'], False)

        self.assertFalse('uuid' in response_body)
        self.assertTrue('errorMessage' in response_body)

        # Test User exists
        self.assertEquals(models.User.objects
                          .filter(email='tim@example.com')
                          .count(),
                          1)

    def test_add_user_no_password(self):
        data = {
            'first_name': 'Tim',
            'last_name': 'Clough',
            'email': 'tim3@example.com',
        }

        # Should fail
        response = self.client.post('/api/users/', data)
        self.assertEquals(response.status_code, status.HTTP_400_BAD_REQUEST)

        # Test User exists
        self.assertEquals(models.User.objects
                          .filter(email='tim3@example.com')
                          .count(),
                          0)


class ExistingUserTestCase(TransactionTestCase):
    def setUp(self):
        self.client = APIClient()
        models.User.objects.create_user(
            first_name='Tim',
            last_name='Clough',
            email='tim@example.com',
            password='hunter2'
        )

        # Get access token
        data = {
            'email': 'tim@example.com',
            'password': 'hunter2'
        }

        response = self.client.post('/api/token/', data)
        access = response.data['access']
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {access}')

    def test_update_password(self):
        uuid = models.User.objects.get(email='tim@example.com').uuid

        data = {
            'password': 'hunter3'
        }

        response = self.client.post(f'/api/users/{uuid}/', data)
        self.assertEquals(response.status_code, status.HTTP_200_OK)

        response_body = response.data

        self.assertTrue('success' in response_body)
        self.assertEquals(response_body['success'], True)

        self.assertFalse('errorMessage' in response_body)

        user = models.User.objects.get(email='tim@example.com')

        self.assertTrue(check_password('hunter3', user.password))
