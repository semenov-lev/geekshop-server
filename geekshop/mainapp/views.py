from django.shortcuts import render

# Create your views here.


def index(request):
    context = {
        'title': 'geekShop',
    }
    return render(request, 'mainapp/index.html', context)


def products(request):
    context = {
        'title': 'geekShop - Каталог',
    }
    return render(request, 'mainapp/products.html', context)
