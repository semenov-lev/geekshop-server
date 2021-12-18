from django.urls import path
from .views import basked_add, basket_remove, basket_edit

app_name = 'baskets'

urlpatterns = [
    path('add/<int:id>/', basked_add, name='basked_add'),
    path('delete/<int:basked_id>/', basket_remove, name='basket_remove'),
    path('edit/<int:id_basket>/<int:quantity>/', basket_edit, name='basket_edit'),
]
