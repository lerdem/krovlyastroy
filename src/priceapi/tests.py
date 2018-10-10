from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .factories import CommonInfoFactory, ProductFactory
from .models import CommonInfo, Product


class CommonInfoViewSetTests(APITestCase):

    def test_create_account(self):
        url = reverse('priceapi:common-info-list')
        group_info = CommonInfoFactory(
            name=CommonInfo.NAME_CHOICES[0][0],
            type=CommonInfo.TYPE_CHOICES[2][0],
            height=57
        )
        product = ProductFactory(
            group=group_info,
            height=0.45,
            surface=Product.SURFACE_CHOICES[0][0],
            price=135.25
        )

        response = self.client.get(url, format='json')
        data = response.data[0]
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual('Профнастил Н-57',data['name'])
        self.assertEqual('0.45', data['product_set'][0]['height'])
        self.assertEqual('Цинк', data['product_set'][0]['surface'])
        self.assertEqual({'50': 162, '100': 155, '1000': 148}, data['product_set'][0]['price'])
