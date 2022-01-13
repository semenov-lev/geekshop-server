from django.urls import path
from mainapp.views import products, ProductDetail

app_name = 'products'

urlpatterns = [
    path('', products, name='products'),
    path('category/<int:id_category>/', products, name='category'),
    path('detail/<int:pk>/', ProductDetail.as_view(), name='product_detail')
]
