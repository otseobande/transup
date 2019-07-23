from rest_framework.test import APITestCase
from rest_framework import status
from providers.models import Provider

class TestProviderEndpoints(APITestCase):
    def test_create_validation(self):
        response = self.client.post('/api/v1/providers/')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data, {
            'name': ['This field is required.'],
            'email': ['This field is required.'],
            'phone_number': ['This field is required.'],
            'language': ['This field is required.'],
            'currency': ['This field is required.']
        })

    def test_create_success(self):
        request_data = {
            'name': 'Ade williams',
            'email': 'adewillams@gmail.com',
            'phone_number': '+2348131928452',
            'language': 'Idoma',
            'currency': 'NGN'
        }
        response = self.client.post(
            '/api/v1/providers/',
            data=request_data
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(request_data.items() <= response.data.items())

        provider = Provider.objects.get(email=request_data['email'])

        self.assertEqual(provider.name, request_data['name'])

    def test_get(self):
        provider = Provider(**{
            'name': 'Ade williams',
            'email': 'adewillams@gmail.com',
            'phone_number': '+2348131928452',
            'language': 'Idoma',
            'currency': 'NGN'
        })
        provider.save()

        response = self.client.get('/api/v1/providers/')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(list(response.data.keys()), [
            'count',
            'next',
            'previous',
            'results'
        ])

        self.assertTrue(len(response.data['results']) > 0)

    def test_get_one(self):
        provider_data = {
            'name': 'Ade williams',
            'email': 'adewillams@gmail.com',
            'phone_number': '+2348131928452',
            'language': 'Idoma',
            'currency': 'NGN'
        }
        provider = Provider(**provider_data)
        provider.save()

        response = self.client.get('/api/v1/providers/{}/'.format(provider.id))

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertTrue(provider_data.items() <= response.data.items())

    def test_update(self):
        provider_data = {
            'name': 'Ade williams',
            'email': 'adewillams@gmail.com',
            'phone_number': '+2348131928452',
            'language': 'Idoma',
            'currency': 'NGN'
        }
        provider = Provider(**provider_data)
        provider.save()

        response = self.client.patch(
            '/api/v1/providers/{}/'.format(provider.id),
            data={ 'email': 'test@gmail.com' }
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        provider.refresh_from_db()
        self.assertEqual(provider.email, 'test@gmail.com')

    def test_delete(self):
        provider_data = {
            'name': 'Ade williams',
            'email': 'adewillams@gmail.com',
            'phone_number': '+2348131928452',
            'language': 'Idoma',
            'currency': 'NGN'
        }
        provider = Provider(**provider_data)
        provider.save()

        response = self.client.delete(
            '/api/v1/providers/{}/'.format(provider.id)
        )

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

