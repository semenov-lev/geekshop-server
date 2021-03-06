from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, JsonResponse
from django.template.loader import render_to_string
from django.views.generic import TemplateView

from mainapp.mixin import UserDispatchMixin, JSONResponseMixin
from mainapp.models import Product
from .models import Basket


@login_required
def basked_add(request, id):
    if request.is_ajax():
        user = request.user
        product = Product.objects.get(id=id)
        baskets = Basket.objects.filter(user=user, product=product)

        if baskets:
            basket = baskets.first()
            basket.quantity += 1
            basket.save()
        else:
            Basket.objects.create(user=user, product=product, quantity=1)
            products = Product.objects.all()
            context = {'products': products}
            result = render_to_string('mainapp/includes/card.html', context)
            return JsonResponse({'result': result})


# class BaskedAddView(JSONResponseMixin, TemplateView, UserDispatchMixin):
#     def get_context_data(self, **kwargs):
#         context = super(BaskedAddView, self).get_context_data(**kwargs)
#         product = Product.objects.get(id=kwargs.get('id'))
#         baskets = Basket.objects.filter(user=self.request.user, product=product)
#         if baskets:
#             basket = baskets.first()
#             basket.quantity += 1
#             basket.save()
#         else:
#             Basket.objects.create(user=self.request.user, product=product, quantity=1)
#         return context
#
#     def render_to_response(self, context, **response_kwargs):
#         return self.render_to_json_response(context, **response_kwargs)


@login_required
def basket_edit(request, id_basket, quantity):
    if request.is_ajax():
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
def basket_remove(request, basked_id):
    Basket.objects.get(id=basked_id).delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
