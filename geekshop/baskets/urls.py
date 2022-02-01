from django.urls import path

from .views import basket_remove, basket_edit, add_to_basket

app_name = 'baskets'

urlpatterns = [
    path('delete/<int:basket_id>/', basket_remove, name='basket_remove'),
    path('add/<int:id>/', add_to_basket, name='basket_add'),
    path('edit/<int:id_basket>/<int:quantity>/', basket_edit, name='basket_edit'),
]
