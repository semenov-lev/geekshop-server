from django.conf import settings
from django.db import models

from mainapp.models import Product


class Order(models.Model):
    FORMING = 'FM'
    SEND_TO_PROCEED = 'STP'
    PROCEEDED = 'PRD'
    PAID = 'PD'
    READY = 'RDY'
    CANCEL = 'CNL'

    ORDER_STATUS_CHOICES = (
        (FORMING, 'Формируется'),
        (SEND_TO_PROCEED, 'Отправлен в обработку'),
        (PROCEEDED, 'Обрабатывается'),
        (PAID, 'Оплачен'),
        (READY, 'Готов к выдаче'),
        (CANCEL, 'Отменен'),
    )

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created = models.DateTimeField(verbose_name='Создан', auto_now_add=True)
    updated = models.DateTimeField(verbose_name='Обновлен', auto_now=True)
    status = models.CharField(choices=ORDER_STATUS_CHOICES, verbose_name='Статус', max_length=3, default=FORMING)
    is_active = models.BooleanField(verbose_name='Активный', default=True)

    class Meta:
        ordering = ('-created',)
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return f'Текущий заказ {self.pk}'

    # TODO: take out self.orderitems.select_related()

    def get_total_quantity(self):
        items = self.orderitems.select_related()
        return sum(list(map(lambda i: i.quantity, items)))

    def get_total_cost(self):
        items = self.orderitems.select_related()
        return sum(list(map(lambda i: i.get_product_cost(), items)))

    def delete(self, using=None, keep_parents=False):
        for item in self.orderitems.select_related():
            item.product.quantity += item.quantity
            item.save()
            self.is_active = False
            self.save()


class OrderItem(models.Model):
    order = models.ForeignKey(Order, verbose_name='Заказ', related_name='orderitems', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, verbose_name='Продукт', on_delete=models.CASCADE)
    quantity = models.IntegerField(verbose_name='Количество', default=0)

    def get_product_cost(self):
        return self.product.price * self.quantity

    @staticmethod
    def get_item(pk):
        return OrderItem.objects.get(pk=pk).quantity
