from django.db import transaction
from django.db.models.signals import pre_save, pre_delete
from django.dispatch import receiver
from django.forms import inlineformset_factory
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView

from baskets.models import Basket
from mainapp.mixin import BaseClassContextMixin
from ordersapp.forms import OrderItemsForm
from ordersapp.models import Order, OrderItem


class OrdersListView(ListView, BaseClassContextMixin):
    model = Order
    template_name = 'ordersapp/order_list.html'
    title = 'GeekShop | Список заказов'


class OrdersCreateView(CreateView, BaseClassContextMixin):
    model = Order
    fields = []
    success_url = reverse_lazy('ordersapp:list')
    title = 'GeekShop | Оформить заказ'

    def get_context_data(self, **kwargs):
        context = super(OrdersCreateView, self).get_context_data(**kwargs)
        OrderFormSet = inlineformset_factory(Order, OrderItem, form=OrderItemsForm, extra=1)
        basket_item = Basket.objects.filter(user=self.request.user)

        if self.request.POST:
            formset = OrderFormSet(self.request.POST)
            basket_item.delete()
        else:
            if basket_item:
                OrderFormSet = inlineformset_factory(Order, OrderItem, form=OrderItemsForm, extra=basket_item.count())
                formset = OrderFormSet()
                for count, form in enumerate(formset.forms):
                    form.initial['product'] = basket_item[count].product
                    form.initial['quantity'] = basket_item[count].quantity
                    form.initial['price'] = basket_item[count].product.price
            else:
                formset = OrderFormSet()
        context['orderitems'] = formset
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        formset = context['orderitems']

        with transaction.atomic():
            form.instance.user = self.request.user
            self.object = form.save()
            if formset.is_valid():
                formset.instance = self.object
                formset.save()

        if self.object.get_total_cost == 0:
            self.object.delete()

        return super(OrdersCreateView, self).form_valid(form)


class OrdersDetailView(DetailView, BaseClassContextMixin):
    model = Order
    title = 'GeekShop | Просмотр заказа'


class OrdersUpdateView(UpdateView, BaseClassContextMixin):
    model = Order
    fields = []
    success_url = reverse_lazy('ordersapp:list')
    title = 'GeekShop | Редактирование заказа'

    def get_context_data(self, **kwargs):
        context = super(OrdersUpdateView, self).get_context_data(**kwargs)
        OrderFormSet = inlineformset_factory(Order, OrderItem, form=OrderItemsForm, extra=1)

        if self.request.POST:
            formset = OrderFormSet(self.request.POST, instance=self.object)
        else:
            formset = OrderFormSet(instance=self.object)
            for form in formset:
                if form.instance.pk:
                    form.initial['price'] = form.instance.product.price
        context['orderitems'] = formset
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        formset = context['orderitems']

        with transaction.atomic():
            self.object = form.save()
            if formset.is_valid():
                formset.instance = self.object
                formset.save()

        if self.object.get_total_cost == 0:
            self.object.delete()

        return super(OrdersUpdateView, self).form_valid(form)


class OrdersDeleteView(DeleteView, BaseClassContextMixin):
    model = Order
    success_url = reverse_lazy('ordersapp:list')
    title = 'GeekShop | Удаление заказа'


def order_forming_complete(request, pk):
    order = get_object_or_404(Order, pk=pk)
    order.status = Order.SEND_TO_PROCEED
    order.save()
    return HttpResponseRedirect(reverse('ordersapp:list'))


@receiver(pre_save, sender=Basket)
@receiver(pre_save, sender=OrderItem)
def product_quantity_update_save(sender, instance, **kwargs):
    if instance.pk:
        get_item = instance.get_item(int(instance.pk))
        instance.product.quantity -= instance.quantity - get_item
    else:
        instance.product.quantity -= instance.quantity
    instance.product.save()


@receiver(pre_delete, sender=Basket)
@receiver(pre_delete, sender=OrderItem)
def product_quantity_update_save(sender, instance, **kwargs):
    instance.product.quantity += instance.quantity
    instance.product.save()
