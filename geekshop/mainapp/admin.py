from django.contrib import admin
from .models import ProductCategory, Product

admin.site.register(ProductCategory)
# admin.site.register(Product)


@admin.register(Product)
class Product(admin.ModelAdmin):

    list_display = ('name', 'price', 'quantity',)
    fields = (('name', 'category'), 'description', 'image', ('price', 'quantity'),)
    readonly_fields = ('description',)
    ordering = ('name', 'price',)
    search_fields = ('name',)
