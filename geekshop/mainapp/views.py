from django.views.generic import DetailView, TemplateView, ListView

from .mixin import BaseClassContextMixin
from .models import Product, ProductCategory


class IndexView(TemplateView, BaseClassContextMixin):
    template_name = 'mainapp/index.html'
    title = 'GeekShop'


class CatalogView(ListView):
    paginate_by = 3
    template_name = 'mainapp/products.html'

    def get_queryset(self):
        if self.kwargs:
            products = Product.objects.filter(category=self.kwargs.get('id_category'))
        else:
            products = Product.objects.all()
        return products.order_by('name')

    def get_context_data(self, **kwargs):
        context = super(CatalogView, self).get_context_data(**kwargs)
        context['title'] = 'GeekShop | Каталог'
        context['categories'] = ProductCategory.objects.all()
        return context


class ProductDetail(DetailView):
    model = Product
    template_name = 'mainapp/detail.html'

    def get_context_data(self, **kwargs):
        context = super(ProductDetail, self).get_context_data(**kwargs)
        product = self.get_object()
        context['product'] = product
        return context
