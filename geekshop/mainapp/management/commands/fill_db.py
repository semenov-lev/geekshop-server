import json
from django.core.management.base import BaseCommand
from mainapp.models import ProductCategory, Product
from django.contrib.auth.models import User


def load_from_json(file_name):
    with open(file_name, mode='r', encoding='utf-8') as infile:

        return json.load(infile)


class Command(BaseCommand):
    def handle(self, *args, **options):
        categories = load_from_json('mainapp/fixtures/categories.json')

        ProductCategory.objects.all().delete()
        for category in categories:
            category_fields = category.get('fields')
            new_category = ProductCategory(**category_fields)
            new_category.save()

        products = load_from_json('mainapp/fixtures/products.json')

        Product.objects.all().delete()
        for product in products:
            product_fields = product.get('fields')
            product_category = product_fields.get('category')
            _category = ProductCategory.objects.get(id=product_category)
            product_fields['category'] = _category
            new_product = Product(**product_fields)
            new_product.save()

        User.objects.create_superuser('django', 'django@geekshop.local', 'geekbrains')
