from django.contrib import admin
from .models import CommonInfo, Product


class ProductInline(admin.TabularInline):
    model = Product
    extra = 0
#
#
# class CommentInline(admin.TabularInline):
#     model = models.Comment
#     extra = 0
#
#
class CommonInfoAdmin(admin.ModelAdmin):
    inlines = (ProductInline,)
    list_display = ()
# #
#
#     CHOICES_LIST = (
#         (1, 'НС'),
#         (2, 'ПК'),
#         (3, 'Н')
#     )
#     length = models.PositiveIntegerField(default=0)
#     width = models.PositiveIntegerField(default=0)
admin.site.register(CommonInfo, CommonInfoAdmin)
# admin.site.register(models.Category, filter_horizontal=('photo',))