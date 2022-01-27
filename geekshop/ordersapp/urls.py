from django.urls import path
from ordersapp.views import OrdersListView, OrdersCreateView, OrdersDetailView, OrdersUpdateView, OrdersDeleteView, \
    order_forming_complete, get_product_price

app_name = 'ordersapp'

urlpatterns = [
    path('', OrdersListView.as_view(), name='list'),
    path('create/', OrdersCreateView.as_view(), name='create'),
    path('detail/<int:pk>/', OrdersDetailView.as_view(), name='detail'),
    path('update/<int:pk>/', OrdersUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', OrdersDeleteView.as_view(), name='delete'),
    path('forming_complete/<int:pk>/', order_forming_complete, name='forming_complete'),
    path('forming_complete/<int:pk>/', order_forming_complete, name='forming_complete'),
    path('product/<int:pk>/price/', get_product_price, name='product_price')
]
