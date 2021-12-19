from django.shortcuts import render

from .models import Product


def index(request):
    context = {
        'title': 'GeekShop',
    }
    return render(request, 'mainapp/index.html', context)


def products(request):
    context = {
        'title': 'GeekShop | Каталог',
        'products': Product.objects.all()[:6]
    }
    return render(request, 'mainapp/products.html', context)


def product_detail(request, product_id):
    product = Product.objects.get(id=product_id)
    context = {
        'title': product.name,
        'product': product
    }
    return render(request, 'mainapp/detail.html', context)
