from django.http import HttpResponseRedirect
from django.shortcuts import render
from mainapp.models import Product
from .models import Basket


def basked_add(request, id):
    user = request.user
    product = Product.objects.get(id=id)
    basket = Basket.objects.filter(user=user, product=product)

    if basket:
        basket.first().quantity += 1
        basket.save()
    else:
        Basket.objects.create(user=user, product=product, quantity=1)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
