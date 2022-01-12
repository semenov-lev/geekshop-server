from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from authapp.models import User
from mainapp.models import ProductCategory, Product
from .forms import AdminUserRegisterForm, AdminUserUpdateForm, AdminCategoryForm, AdminProductForm


@user_passes_test(lambda u: u.is_superuser)
def index(request):
    context = {
        'title': 'GeekShop - Администратор'
    }
    return render(request, 'admins/admin.html', context)


@user_passes_test(lambda u: u.is_superuser)
def user_read(request):
    context = {
        'title': 'GeekShop - Администратор | Пользователи',
        'all_users': User.objects.all()
    }
    return render(request, 'admins/admin-users-read.html', context)


@user_passes_test(lambda u: u.is_superuser)
def user_create(request):
    if request.method == 'POST':
        form = AdminUserRegisterForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Вы успешно зарегистрировались!')
            return HttpResponseRedirect(reverse('admins:user_read'))
    else:
        form = AdminUserRegisterForm()
    context = {
        'title': 'GeekShop - Администратор | Создание пользователя',
        'form': form
    }
    return render(request, 'admins/admin-users-create.html', context)


@user_passes_test(lambda u: u.is_superuser)
def user_update(request, pk):
    updated_user = User.objects.get(id=pk)
    if request.method == 'POST':
        form = AdminUserUpdateForm(data=request.POST, instance=updated_user, files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Данные успешно обновлены!')
            return HttpResponseRedirect(reverse('admins:user_read'))
    else:
        form = AdminUserUpdateForm(instance=updated_user)
    context = {
        'title': f'GeekShop - Администратор | Пользователь {updated_user.username}',
        'form': form,
        'updated_user': updated_user
    }
    return render(request, 'admins/admin-users-update-delete.html', context)


@user_passes_test(lambda u: u.is_superuser)
def user_delete(request, pk):
    user = User.objects.get(pk=pk)
    user.is_active = False
    user.save()
    return HttpResponseRedirect(reverse('admins:user_read'))


@user_passes_test(lambda u: u.is_superuser)
def category_read(request):
    context = {
        'title': 'GeekShop - Администратор | Категории продуктов',
        'all_categories': ProductCategory.objects.all()
    }
    return render(request, 'admins/admin-category-read.html', context)


@user_passes_test(lambda u: u.is_superuser)
def category_create(request):
    if request.method == 'POST':
        form = AdminCategoryForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Категория успешно создана')
            return HttpResponseRedirect(reverse('admins:category_read'))
    else:
        form = AdminCategoryForm()
    context = {
        'title': 'GeekShop - Администратор | Создание категории',
        'form': form
    }
    return render(request, 'admins/admin-category-create.html', context)


@user_passes_test(lambda u: u.is_superuser)
def category_update(request, pk):
    updated_category = ProductCategory.objects.get(id=pk)
    if request.method == 'POST':
        form = AdminCategoryForm(data=request.POST, instance=updated_category)
        if form.is_valid():
            form.save()
            messages.success(request, 'Данные успешно обновлены!')
            return HttpResponseRedirect(reverse('admins:category_read'))
    else:
        form = AdminCategoryForm(instance=updated_category)
    context = {
        'title': f'GeekShop - Администратор | Изменение категории {updated_category.name}',
        'form': form,
        'updated_category': updated_category
    }
    return render(request, 'admins/admin-category-update-delete.html', context)


@user_passes_test(lambda u: u.is_superuser)
def category_delete(request, pk):
    category = ProductCategory.objects.get(pk=pk)
    category.delete()
    return HttpResponseRedirect(reverse('admins:category_read'))


@user_passes_test(lambda u: u.is_superuser)
def product_read(request):
    context = {
        'title': 'GeekShop - Администратор | Продукты',
        'all_products': Product.objects.all()
    }
    return render(request, 'admins/admin-product-read.html', context)


@user_passes_test(lambda u: u.is_superuser)
def product_create(request):
    if request.method == 'POST':
        form = AdminProductForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Продукт успешно создан')
            return HttpResponseRedirect(reverse('admins:product_read'))
    else:
        form = AdminProductForm()
    context = {
        'title': 'GeekShop - Администратор | Создание продукта',
        'form': form
    }
    return render(request, 'admins/admin-product-create.html', context)


@user_passes_test(lambda u: u.is_superuser)
def product_update(request, pk):
    updated_product = Product.objects.get(id=pk)
    if request.method == 'POST':
        form = AdminProductForm(data=request.POST, instance=updated_product, files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Данные успешно обновлены!')
            return HttpResponseRedirect(reverse('admins:product_read'))
    else:
        form = AdminProductForm(instance=updated_product)
    context = {
        'title': f'GeekShop - Администратор | {updated_product.name}',
        'form': form,
        'updated_product': updated_product
    }
    return render(request, 'admins/admin-product-update-delete.html', context)


@user_passes_test(lambda u: u.is_superuser)
def product_delete(request, pk):
    product = Product.objects.get(pk=pk)
    product.delete()
    return HttpResponseRedirect(reverse('admins:product_read'))
