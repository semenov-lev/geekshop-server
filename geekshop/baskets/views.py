from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import redirect
from django.template.loader import render_to_string

from mainapp.models import Product
from .models import Basket


@login_required
def add_to_basket(request, id):
    product = Product.objects.get(id=id)
    baskets = Basket.objects.filter(user=request.user, product=product)
    if baskets:
        basket = baskets.first()
        basket.quantity += 1
        basket.save()
    else:
        Basket.objects.create(user=request.user, product=product, quantity=1)
    return redirect(request.META.get('HTTP_REFERER'))


@login_required
def basket_edit(request, id_basket, quantity):
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        basket = Basket.objects.get(id=id_basket)
        if quantity > 0:
            basket.quantity = quantity
            basket.save()
        else:
            basket.delete()

        baskets = Basket.objects.filter(user=request.user)
        context = {
            'baskets': baskets
        }
        result = render_to_string('baskets/basket.html', context)
        return JsonResponse({'result': result})


@login_required
def basket_remove(request, basket_id):
    Basket.objects.get(id=basket_id).delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
