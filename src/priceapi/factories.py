import factory


class CommonInfoFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'priceapi.CommonInfo'


class ProductFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'priceapi.Product'

    group = factory.SubFactory(CommonInfoFactory)
    height = factory.Sequence(lambda n: n/10)
    surface = 2
    price = factory.Sequence(lambda n: n*10)
