from django.contrib import admin

from .models import CommonInfo, Product


class ProductInline(admin.TabularInline):
    model = Product
    extra = 0


class CommonInfoAdmin(admin.ModelAdmin):
    inlines = (ProductInline,)
    list_display = ('name', 'type', 'height')

admin.site.register(CommonInfo, CommonInfoAdmin)
admin.site.register(Product)
# admin.site.register(models.Category, filter_horizontal=('photo',))
