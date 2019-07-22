from rest_framework.test import APITestCase
from rest_framework import status

class TestIndexEndpoints(APITestCase):
    def test_base_endpoint(self):
        response = self.client.get('/')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['message'], 'Welcome to Transup')

    def test_api_base_endpoint(self):
        response = self.client.get('/')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['message'], 'Welcome to Transup')

    def test_v1_api_base_endpoint(self):
        response = self.client.get('/')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['message'], 'Welcome to Transup')


