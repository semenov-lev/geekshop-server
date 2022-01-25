from django.shortcuts import render
from django.views.generic import TemplateView, ListView

from mainapp.mixin import BaseClassContextMixin
from ordersapp.models import Order


class OrdersListView(ListView, BaseClassContextMixin):
    model = Order
    template_name = 'ordersapp/order_list.html'
    title = 'Заказы | Список заказов'


class OrdersCreateView(TemplateView):
    pass


class OrdersDetailView(TemplateView):
    pass


class OrdersUpdateView(TemplateView):
    pass


class OrdersDeleteView(TemplateView):
    pass
