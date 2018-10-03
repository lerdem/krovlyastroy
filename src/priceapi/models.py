from django.db import models


class BasicModel(models.Model):
    created = models.DateField(auto_now=True)
    updated = models.DateField(auto_now_add=True)

    class Meta:
        abstract = True


class CommonInfo(BasicModel):
    TYPE_CHOICES = (
        (1, 'НС'),
        (2, 'ПК'),
        (3, 'Н')
    )

    NAME_CHOICES = (
        (1, 'Профнастил'),
        (2, 'Металлочерепица'),
        (3, 'Мансардное окно')
    )
    name = models.PositiveSmallIntegerField(choices=NAME_CHOICES, default=1)
    type = models.PositiveSmallIntegerField(choices=TYPE_CHOICES, default=1)
    height = models.PositiveIntegerField(default=20)

    class Meta:
        verbose_name_plural = 'Продукты'
        verbose_name = 'Продукты'

    def __str__(self):
        return '{name} {type}-{height}'.format(
            name=self.get_name_display(),
            type=self.get_type_display(),
            height=self.height
        )


class Product(BasicModel):

    SURFACE_CHOICES = (
        (1, 'Цинк'),
        (2, '3D Декоративный'),
        (3, 'Полиестер матовый PEMA'),
        (4, 'Полиестер PE')
    )

    group = models.ForeignKey('CommonInfo', on_delete=models.CASCADE)
    height = models.DecimalField(max_digits=3, decimal_places=2, help_text='толщина металла')
    surface = models.PositiveIntegerField(choices=SURFACE_CHOICES, help_text='тип покрытия')
    price = models.DecimalField(max_digits=5, decimal_places=2)

    class Meta:
        verbose_name_plural = 'Свойства'
        verbose_name = 'Свойства'

    def __str__(self):
        return '`{surface}`-{height}: {price}, грн.'.format(
            height=self.height,
            surface=self.get_surface_display(),
            price=self.price,
        )

    @property
    def get_price_for_sale(self):
        return {
            '50': 20,
            '100': 15,
            '1000': 10,
        }
