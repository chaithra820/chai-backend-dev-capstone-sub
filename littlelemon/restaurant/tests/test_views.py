from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status

class MenuViewTest(APITestCase):
    def test_get_menu(self):
        response = self.client.get('/api/menu/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
