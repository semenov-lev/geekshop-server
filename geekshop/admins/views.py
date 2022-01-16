from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView

from authapp.models import User
from mainapp.mixin import BaseClassContextMixin, AdminDispatchMixin
from mainapp.models import ProductCategory, Product
from .forms import AdminUserRegisterForm, AdminUserUpdateForm, AdminCategoryForm, AdminProductForm


class AdminIndexView(TemplateView, BaseClassContextMixin, AdminDispatchMixin):
    title = 'GeekShop - Администратор'
    template_name = 'admins/admin.html'


class UserListView(ListView, BaseClassContextMixin, AdminDispatchMixin):
    model = User
    template_name = 'admins/admin-users-read.html'
    title = 'GeekShop - Администратор | Пользователи'


class UserCreateView(CreateView, BaseClassContextMixin, AdminDispatchMixin):
    model = User
    template_name = 'admins/admin-users-create.html'
    title = 'GeekShop - Администратор | Создание пользователя'
    form_class = AdminUserRegisterForm
    success_url = reverse_lazy('admins:user_read')


class UserUpdateView(UpdateView, BaseClassContextMixin, AdminDispatchMixin):
    model = User
    template_name = 'admins/admin-users-update-delete.html'
    title = 'GeekShop - Администратор | Изменение пользователя'
    form_class = AdminUserUpdateForm
    success_url = reverse_lazy('admins:user_read')


class UserDeleteView(DeleteView, AdminDispatchMixin):
    model = User
    template_name = 'admins/admin-users-update-delete.html'
    success_url = reverse_lazy('admins:user_read')
    object = None

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.is_active = False
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


class CategoryListView(ListView, BaseClassContextMixin, AdminDispatchMixin):
    model = ProductCategory
    template_name = 'admins/admin-category-read.html'
    title = 'GeekShop - Администратор | Категории продуктов'


class CategoryCreateView(CreateView, BaseClassContextMixin, AdminDispatchMixin):
    model = ProductCategory
    template_name = 'admins/admin-category-create.html'
    title = 'GeekShop - Администратор | Создание категории'
    form_class = AdminCategoryForm
    success_url = reverse_lazy('admins:category_read')


class CategoryUpdateView(UpdateView, BaseClassContextMixin, AdminDispatchMixin):
    model = ProductCategory
    template_name = 'admins/admin-category-update-delete.html'
    title = 'GeekShop - Администратор | Изменение категории'
    form_class = AdminCategoryForm
    success_url = reverse_lazy('admins:category_read')


class CategoryDeleteView(DeleteView, AdminDispatchMixin):
    model = ProductCategory
    success_url = reverse_lazy('admins:category_read')


class ProductListView(ListView, BaseClassContextMixin, AdminDispatchMixin):
    model = Product
    template_name = 'admins/admin-product-read.html'
    title = 'GeekShop - Администратор | Продукты'


class ProductCreateView(CreateView, BaseClassContextMixin, AdminDispatchMixin):
    model = Product
    template_name = 'admins/admin-product-create.html'
    title = 'GeekShop - Администратор | Создание продукта'
    form_class = AdminProductForm
    success_url = reverse_lazy('admins:product_read')


class ProductUpdateView(UpdateView, BaseClassContextMixin, AdminDispatchMixin):
    model = Product
    template_name = 'admins/admin-product-update-delete.html'
    title = 'GeekShop - Администратор | Редактирование товара'
    form_class = AdminProductForm
    success_url = reverse_lazy('admins:product_read')


class ProductDeleteView(DeleteView, AdminDispatchMixin):
    model = Product
    success_url = reverse_lazy('admins:product_read')
