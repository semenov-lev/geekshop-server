from django.urls import path
from .views import index, user_create, user_read, user_update, user_delete, category_read, category_create, \
    category_update, category_delete, product_read, product_create, product_update, product_delete

app_name = 'admins'

urlpatterns = [
    path('', index, name='index'),
    path('users/', user_read, name='user_read'),
    path('users-create/', user_create, name='user_create'),
    path('users-update/<int:pk>', user_update, name='user_update'),
    path('users-delete/<int:pk>', user_delete, name='user_delete'),
    path('category/', category_read, name='category_read'),
    path('category-create/', category_create, name='category_create'),
    path('category-update/<int:pk>', category_update, name='category_update'),
    path('category-delete/<int:pk>', category_delete, name='category_delete'),
    path('product/', product_read, name='product_read'),
    path('product-create/', product_create, name='product_create'),
    path('product-update/<int:pk>', product_update, name='product_update'),
    path('product-delete/<int:pk>', product_delete, name='product_delete'),
]
