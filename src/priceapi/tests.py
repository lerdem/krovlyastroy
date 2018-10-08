from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .factories import CommonInfoFactory, ProductFactory


class CommonInfoViewSetTests(APITestCase):
    def test_create_account(self):
        url = reverse('priceapi:common-info-list')
        group_info = CommonInfoFactory()
        ProductFactory(group=group_info)

        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
