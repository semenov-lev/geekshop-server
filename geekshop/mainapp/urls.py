from django.urls import path
from mainapp.views import ProductDetail, CatalogView

app_name = 'products'

urlpatterns = [
    path('', CatalogView.as_view(), name='products'),
    path('category/<int:id_category>/', CatalogView.as_view(), name='category'),
    path('detail/<int:pk>/', ProductDetail.as_view(), name='product_detail'),
]
