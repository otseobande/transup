from django.test import TestCase

# Create your tests here.
from rest_framework.test import APITestCase
from rest_framework import status
from serviceareas.models import ServiceArea
from providers.models import Provider

provider = Provider(**{
    'name': 'Ade williams',
    'email': 'adewilms@gmail.com',
    'phone_number': '+2348131928452',
    'language': 'Idoma',
    'currency': 'NGN'
})
provider.save()

class TestServiceAreaEndpoints(APITestCase):
    def test_create_validation(self):
        response = self.client.post('/api/v1/service-areas/')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data, {
             "name": [
                "This field is required."
            ],
            "price": [
                "This field is required."
            ],
            "provider": [
                "This field is required."
            ],
            "coordinates": [
                "This field is required."
            ]
        })


    def test_get(self):
        service_area = ServiceArea(**{
            "name": "J park",
            "price": "5.10",
            "provider_id": provider.id,
            "coordinates": [[23,32], [32, 42], [23, 27], [23,32]]
        })
        service_area.save()

        response = self.client.get('/api/v1/service-areas/')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(list(response.data.keys()), [
            'count',
            'next',
            'previous',
            'results'
        ])

        self.assertTrue(len(response.data['results']) > 0)

    def test_get_one(self):
        service_area_data = {
            "name": "J park",
            "price": "5.10",
            "provider_id": provider.id,
            "coordinates": [[23,32], [32, 42], [23, 27], [23,32]]
        }
        service_area = ServiceArea(**service_area_data)
        service_area.save()

        response = self.client.get('/api/v1/service-areas/{}/'.format(service_area.id))

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update(self):
        service_area_data = {
            "name": "J park",
            "price": "5.10",
            "provider_id": provider.id,
            "coordinates": [[23,32], [32, 42], [23, 27], [23,32]]
        }
        service_area = ServiceArea(**service_area_data)
        service_area.save()

        response = self.client.patch(
            '/api/v1/service-areas/{}/'.format(service_area.id),
            data={ 'name': 'test name' }
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        service_area.refresh_from_db()
        self.assertEqual(service_area.name, 'test name')

    def test_delete(self):
        service_area_data = {
            "name": "J park",
            "price": "5.10",
            "provider_id": provider.id,
            "coordinates": [[23,32], [32, 42], [23, 27], [23,32]]
        }
        service_area = ServiceArea(**service_area_data)
        service_area.save()

        response = self.client.delete(
            '/api/v1/service-areas/{}/'.format(service_area.id)
        )

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

