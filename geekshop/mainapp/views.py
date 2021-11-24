from django.shortcuts import render

from .models import Product


def index(request):
    context = {
        'title': 'geekShop',
    }
    return render(request, 'mainapp/index.html', context)


def products(request):
    context = {
        'title': 'geekShop - Каталог',
        'products': Product.objects.all()[:6]
    }
    return render(request, 'mainapp/products.html', context)
