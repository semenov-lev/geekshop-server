from django.shortcuts import render
from django.views.generic import DetailView

from .models import Product, ProductCategory


def index(request):
    context = {
        'title': 'GeekShop',
    }
    return render(request, 'mainapp/index.html', context)


def products(request, id_category=None):
    context = {
        'title': 'GeekShop | Каталог',
        'categories': ProductCategory.objects.all(),
    }
    if id_category:
        context['products'] = Product.objects.filter(category=id_category)
    else:
        context['products'] = Product.objects.all()
    return render(request, 'mainapp/products.html', context)


class ProductDetail(DetailView):
    model = Product
    template_name = 'mainapp/detail.html'

    def get_context_data(self, **kwargs):
        context = super(ProductDetail, self).get_context_data(**kwargs)
        product = self.get_object()
        context['product'] = product
        return context
