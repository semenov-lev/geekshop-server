from django.urls import path
from .views import AdminIndexView, UserListView, UserCreateView, UserUpdateView, UserDeleteView, CategoryListView, \
    CategoryCreateView, CategoryUpdateView, CategoryDeleteView, ProductListView, ProductCreateView, ProductUpdateView, \
    ProductDeleteView

app_name = 'admins'

urlpatterns = [
    path('', AdminIndexView.as_view(), name='index'),
    path('users/', UserListView.as_view(), name='user_read'),
    path('users-create/', UserCreateView.as_view(), name='user_create'),
    path('users-update/<int:pk>', UserUpdateView.as_view(), name='user_update'),
    path('users-delete/<int:pk>', UserDeleteView.as_view(), name='user_delete'),
    path('category/', CategoryListView.as_view(), name='category_read'),
    path('category-create/', CategoryCreateView.as_view(), name='category_create'),
    path('category-update/<int:pk>', CategoryUpdateView.as_view(), name='category_update'),
    path('category-delete/<int:pk>', CategoryDeleteView.as_view(), name='category_delete'),
    path('product/', ProductListView.as_view(), name='product_read'),
    path('product-create/', ProductCreateView.as_view(), name='product_create'),
    path('product-update/<int:pk>', ProductUpdateView.as_view(), name='product_update'),
    path('product-delete/<int:pk>', ProductDeleteView.as_view(), name='product_delete'),
]
