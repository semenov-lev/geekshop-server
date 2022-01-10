from django.db import models


class ProductCategory(models.Model):
    name = models.CharField(verbose_name='Наименование категории', max_length=64, unique=True)
    description = models.TextField(verbose_name='Описание категории', blank=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    name = models.CharField(verbose_name='Наименование товара', max_length=60, unique=True)
    image = models.ImageField(upload_to='products_images', blank=True)
    short_description = models.TextField(verbose_name='Краткое описание', max_length=128, blank=True)
    description = models.TextField(verbose_name='Описание продукта', blank=True)
    price = models.DecimalField(verbose_name='Цена', max_digits=8, decimal_places=2, default=0)
    quantity = models.PositiveIntegerField(verbose_name='Количество на складе', blank=True)

    def __str__(self):
        return f'{self.name} | {self.category.name}'
