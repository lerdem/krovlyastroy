from django.db import models

# Create your models here.


class BasicModel(models.Model):
    created = models.DateField(auto_now=True)
    updated = models.DateField(auto_now_add=True)

    class Meta:
        abstract = True


class CommonInfo(BasicModel):
    CHOICES_LIST = (
        (1, 'НС'),
        (2, 'ПК'),
        (3, 'Н')
    )
    type = models.PositiveSmallIntegerField(choices=CHOICES_LIST, default=1)
    length = models.PositiveIntegerField(default=0)
    width = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name_plural = 'Продукты'
        verbose_name = 'Продукты'


class Product(BasicModel):
    group = models.ForeignKey('CommonInfo', on_delete=models.CASCADE)
    height = models.PositiveIntegerField(default=0)
    price = models.DecimalField(max_digits=5, decimal_places=2)