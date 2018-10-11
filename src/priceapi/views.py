import collections
from ipaddress import ip_address, ip_network

import requests
from django.http import HttpResponse, HttpResponseForbidden
from django.views.decorators.csrf import csrf_exempt
from rest_framework import decorators, filters, mixins, serializers, viewsets

from .models import CommonInfo, Product


@csrf_exempt
def hello(request):
    # Verify if request came from GitHub
    forwarded_for = u'{}'.format(request.META.get('HTTP_X_FORWARDED_FOR'))
    client_ip_address = ip_address(forwarded_for)
    whitelist = requests.get('https://api.github.com/meta').json()['hooks']

    for valid_ip in whitelist:
        if client_ip_address in ip_network(valid_ip):
            break
    else:
        return HttpResponseForbidden('Permission denied.')

    event = request.META.get('HTTP_X_GITHUB_EVENT', 'ping')

    return HttpResponse(event)


class ProductSerializer(serializers.ModelSerializer):
    surface = serializers.CharField(source='get_surface_display', read_only=True)
    price = serializers.SerializerMethodField()

    def get_price(self, obj):
        res = {}
        for k,v in obj.get_price_for_sale.items():
            percent = 1 + (v / 100)
            res[k] = int(float(obj.price) * percent)
        return res

    class Meta:
        model = Product
        fields = (
            'height',
            'surface',
            'price',
        )


# Serializers define the API representation.
class CommonInfoSerializer(serializers.ModelSerializer):
    product_set = ProductSerializer(
        many=True,
        read_only=True
    )
    name = serializers.SerializerMethodField()

    def get_name(self, obj):
        return '{name} {type}-{height}'.format(
            name=obj.get_name_display(),
            type=obj.get_type_display(),
            height=obj.height
        )

    class Meta:
        model = CommonInfo
        fields = (
            'name',
            'product_set',
        )


class SchemaOrgMarckUpSerializer(ProductSerializer):
    # name = serializers.CharField(source='group.get_name_display')
    name = serializers.SerializerMethodField()

    def get_name(self, obj):
        obj = obj.group
        return '{name} {type}-{height}'.format(
            name=obj.get_name_display(),
            type=obj.get_type_display(),
            height=obj.height
        )

    class Meta:
        model = Product
        fields = (
            'height',
            'surface',
            'price',
            'name'
        )

    def to_representation(self, instance):
        instance = super().to_representation(instance)
        return collections.OrderedDict({
            "@context": "http://schema.org/",
            "@type": "Product",
            "name": instance['name'],
            "description": "Купить {name} Днепр, толщина - {height} мм, поверхность - {surface}, "
                           "цена от {max_price} грн.".format(
                name=instance['name'],
                surface=instance['surface'],
                max_price=instance['price']['1000'],
                height=instance['height'],
            ),
            "brand": {
                "@type": "Thing",
                "name": "Кровля Строй"
            },
            # "aggregateRating": {
            #     "@type": "AggregateRating",
            #     "ratingValue": "4.4",
            #     "ratingCount": "89"
            # },
            "offers": {
                "@type": "AggregateOffer",
                "lowPrice": instance['price']['1000'],
                "highPrice": instance['price']['50'],
                "priceCurrency": "UAH"
            }
        })


# ViewSets define the view behavior.
class CommonInfoViewSet(mixins.ListModelMixin,
                        viewsets.GenericViewSet):
    def get_queryset(self):
        if self.action == 'schema_org':
            return Product.objects.all()
        return CommonInfo.objects.all()

    filter_backends = (filters.OrderingFilter,)
    ordering = ('height',)

    def get_serializer_class(self):
        if self.action == 'schema_org':
            return SchemaOrgMarckUpSerializer
        return CommonInfoSerializer

    @decorators.action(detail=False)
    def schema_org(self, request, *args, **kwargs):
        return self.list(self.serializer_class)
