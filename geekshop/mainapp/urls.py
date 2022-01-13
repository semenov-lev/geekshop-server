from django.urls import path
from mainapp.views import catalog, ProductDetail

app_name = 'products'

urlpatterns = [
    path('', catalog, name='products'),
    path('category/<int:id_category>/', catalog, name='category'),
    path('page/<int:page>/', catalog, name='page'),
    path('detail/<int:pk>/', ProductDetail.as_view(), name='product_detail'),
]
