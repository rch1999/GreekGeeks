from django.test import TestCase, TransactionTestCase
from django.contrib.auth.hashers import check_password
from rest_framework.test import APIClient
from rest_framework import status
import api.models as models
import uuid


class ApiBaseTestCase(TransactionTestCase):
    PASS = 'hunter2'

    def setUp(self):
        self.client = APIClient()

    def authorize(self, email, password):
        data = {
            'email': self.user.email,
            'password': ApiBaseTestCase.PASS
        }

        response = self.client.post(
            '/api/token/',
            data
        )

        access = response.data['access']
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {access}')

    def make_org1(self):
        org = models.Organization(
            institution='School 1',
            organization_name='Organization 1',
            chapter_name='Chapter 1'
        )
        return org

    def make_org2(self):
        org = models.Organization(
            institution='School 2',
            organization_name='Organization 2',
            chapter_name='Chapter 2'
        )
        return org

    def make_user1(self):
        user = models.User.objects.create_user(
            first_name='Tim',
            last_name='Clough',
            email='tim@example.com',
            password=ApiBaseTestCase.PASS
        )
        return user

    def make_user2(self):
        user = models.User.objects.create_user(
            first_name='Bilbo',
            last_name='Baggins',
            email='baggins@shire.com',
            password=ApiBaseTestCase.PASS
        )
        return user

    def make_contact1(self, org, user):
        contact = models.Contact(
            organization=org,
            created_by=user,
            first_name='Joe',
            last_name='Schmoe'
        )
        return contact

    def make_contact2(self, org, user):
        contact = models.Contact(
            organization=org,
            created_by=user,
            first_name='Caleb',
            last_name='Smith'
        )
        return contact

    def make_rank1(self, org):
        rank = models.ContactRank(
            organization=org,
            name='A',
            description='Interested in signing bid'
        )
        return rank


class TokenTestCase(ApiBaseTestCase):
    def setUp(self):
        super().setUp()
        self.user = self.make_user1()
        self.user.save()

        self.user2 = self.make_user2()

    def test_token_valid_credentials(self):
        data = {
            'email': self.user.email,
            'password': ApiBaseTestCase.PASS
        }

        response = self.client.post(
            '/api/token/',
            data
        )
        self.assertEquals(response.status_code, status.HTTP_200_OK)

        response_body = response.data

        self.assertTrue('access' in response_body)
        self.assertTrue('refresh' in response_body)

    def test_token_invalid_credentials(self):
        data = {
            'email': self.user2.email,
            'password': ApiBaseTestCase.PASS
        }

        response = self.client.post(
            '/api/token/',
            data
        )
        self.assertEquals(response.status_code, status.HTTP_401_UNAUTHORIZED)

        response_body = response.data

        self.assertTrue('access' not in response_body)
        self.assertTrue('refresh' not in response_body)


class ContactsTestCase(ApiBaseTestCase):
    def setUp(self):
        super().setUp()

        self.org = self.make_org1()
        self.org.save()
        self.user = self.make_user1()
        self.user.save()
        self.org.users.add(self.user)
        self.org.save()
        self.contact = self.make_contact1(self.org, self.user)
        self.contact.save()

        self.contact2 = self.make_contact2(self.org, self.user)

        self.rank = self.make_rank1(self.org)
        self.rank.save()

        self.authorize(self.user.email, ApiBaseTestCase.PASS)

    def test_get_contacts(self):
        response = self.client.get(
            f'/api/organizations/{self.org.uuid}/contacts/'
        )
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEquals(len(response.data), 1)

    def test_post_contacts(self):
        data = {
            'first_name': self.contact2.first_name,
            'last_name': self.contact2.last_name,
            'organization_uuid': self.org.uuid,
            'rank_uuid': self.rank.uuid,
            'primary_contact_method': {
                'phone',
                '(123)-456-7890'
            }
        }
        response = self.client.post(
            f'/api/organizations/{self.org.uuid}/contacts/',
            data
        )
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)
        response_body = response.data
        self.assertTrue('success' in response_body)
        self.assertEquals(response_body['success'], True)

        self.assertTrue('uuid' in response_body)
        self.assertFalse('errorMessage' in response_body)

        # test contact exists
        self.assertEquals(
            models.Organization.objects.get(uuid=self.org.uuid)
                  .contact_set.filter(uuid=response_body['uuid']).count(),
            1
        )


class ContactTestCase(ApiBaseTestCase):
    def setUp(self):
        super().setUp()

        self.org = self.make_org1()
        self.org.save()

        self.user = self.make_user1()
        self.user.save()
        self.org.users.add(self.user)

        self.contact = self.make_contact1(self.org, self.user)
        self.contact.save()

        self.contact2 = self.make_contact2(self.org, self.user)
        self.contact2.save()

        self.authorize(self.user.email, ApiBaseTestCase.PASS)

    def test_get_contact(self):
        response = self.client.get(
            f'/api/organizations/{self.org.uuid}/contacts/{self.contact.uuid}/'
        )
        self.assertEquals(response.status_code, status.HTTP_200_OK)

        self.assertEquals(
            uuid.UUID(response.data['uuid']),
            self.contact.uuid
        )

    def test_post_contact(self):
        data = {
            'first_name': 'XYZ',
            'last_name': 'ABC'
        }
        response = self.client.post(
            f'/api/organizations/{self.org.uuid}/contacts/{self.contact.uuid}/',
            data
        )

        self.assertEquals(response.status_code, status.HTTP_200_OK)

        self.assertEquals(response.data['success'], True)

        self.contact.refresh_from_db()
        self.assertEquals(
            self.contact.first_name,
            'XYZ'
        )
        self.assertEquals(
            self.contact.last_name,
            'ABC'
        )

    def test_delete_contact(self):
        response = self.client.delete(
            f'/api/organizations/{self.org.uuid}/contacts/{self.contact2.uuid}/'
        )

        self.assertEquals(response.status_code, status.HTTP_200_OK)

        self.assertEquals(response.data['success'], True)
        self.assertFalse('errorMessage' in response.data)

        self.assertEquals(
            self.org.contact_set
                .filter(uuid=self.contact2.uuid).count(),
            0
        )


class CreateUserTestCase(ApiBaseTestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = self.make_user1()
        self.user.save()

        # not saved
        self.user2 = self.make_user2()

    def test_add_user_successful(self):
        data = {
            'first_name': self.user2.first_name,
            'last_name': self.user2.last_name,
            'email': self.user2.email,
            'password': ApiBaseTestCase.PASS
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
                          .filter(email=self.user2.email)
                          .count(),
                          1)

    def test_add_user_duplicate(self):
        data = {
            'first_name': self.user.first_name,
            'last_name': self.user.last_name,
            'email': self.user.email,
            'password': ApiBaseTestCase.PASS
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
            'first_name': self.user2.first_name,
            'last_name': self.user2.last_name,
            'email': self.user2.email,
        }

        # Should fail
        response = self.client.post('/api/users/', data)
        self.assertEquals(response.status_code, status.HTTP_400_BAD_REQUEST)

        # Test User exists
        self.assertEquals(models.User.objects
                          .filter(email='tim3@example.com')
                          .count(),
                          0)


class ExistingUserTestCase(ApiBaseTestCase):
    def setUp(self):
        super().setUp()        

        self.user = models.User.objects.create_user(
            first_name='Tim',
            last_name='Clough',
            email='tim@example.com',
            password='hunter2'
        )
        self.user.save()

        self.authorize(self.user.email, ApiBaseTestCase.PASS)

    def test_update_password(self):
        uuid = self.user.uuid

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
