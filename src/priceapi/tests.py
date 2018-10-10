from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .factories import CommonInfoFactory, ProductFactory
from .models import CommonInfo, Product


class CommonInfoViewSetTests(APITestCase):

    def setUp(self):
        group_info = CommonInfoFactory(
            name=CommonInfo.NAME_CHOICES[0][0],
            type=CommonInfo.TYPE_CHOICES[2][0],
            height=57
        )
        ProductFactory(
            group=group_info,
            height=0.45,
            surface=Product.SURFACE_CHOICES[0][0],
            price=135.25
        )

    def test_get_list_products(self):
        url = reverse('priceapi:common-info-list')

        response = self.client.get(url, format='json')
        data = response.data[0]
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(1, len(response.data))
        self.assertEqual('Профнастил Н-57', data['name'])
        self.assertIn('name', data)
        self.assertIn('product_set', data)
        self.assertEqual('0.45', data['product_set'][0]['height'])
        self.assertEqual('Цинк', data['product_set'][0]['surface'])
        self.assertEqual({'50': 162, '100': 155, '1000': 148}, data['product_set'][0]['price'])

    def test_get_list_schema_org(self):
        url = reverse('priceapi:common-info-schema-org')

        response = self.client.get(url, format='json')
        data = response.data[0]
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(1, len(response.data))
        self.assertIn('description', data)
        self.assertIn('offers', data)
        self.assertIn('name', data)
        # TODO
        # self.assertDictEqual()
        # https://medium.com/grammofy/testing-your-python-api-app-with-json-schema-52677fe73351