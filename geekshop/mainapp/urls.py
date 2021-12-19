from django.urls import path
from mainapp.views import products, product_detail

app_name = 'products'

urlpatterns = [
    path('', products, name='products'),
    path('detail/<int:product_id>/', product_detail, name='product_detail')
]
