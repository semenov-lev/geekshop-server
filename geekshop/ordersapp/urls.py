from django.urls import path
from mainapp.views import ProductDetail, CatalogView
from ordersapp.views import OrdersListView, OrdersCreateView, OrdersDetailView, OrdersUpdateView, OrdersDeleteView

app_name = 'ordersapp'

urlpatterns = [
    path('', OrdersListView.as_view(), name='list'),
    path('create/', OrdersCreateView.as_view(), name='create'),
    path('detail/', OrdersDetailView.as_view(), name='detail'),
    path('update/', OrdersUpdateView.as_view(), name='update'),
    path('delete/', OrdersDeleteView.as_view(), name='delete'),
]
