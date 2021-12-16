from django.http import HttpResponseRedirect
from django.shortcuts import render
from mainapp.models import Product
from .models import Basket


def basked_add(request, id):
    user = request.user
    product = Product.objects.get(id=id)
    baskets = Basket.objects.filter(user=user, product=product)

    if baskets:
        basket = baskets.first()
        basket.quantity += 1
        basket.save()
    else:
        Basket.objects.create(user=user, product=product, quantity=1)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def basket_remove(request, basked_id):
    Basket.objects.get(id=basked_id).delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
