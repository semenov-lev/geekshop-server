from django.urls import path
from .views import basked_add
from .views import basket_remove

app_name = 'baskets'

urlpatterns = [
    path('add/<int:id>/', basked_add, name='basked_add'),
    path('delete/<int:basked_id>/', basket_remove, name='basket_remove'),
]
