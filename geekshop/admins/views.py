from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from authapp.models import User
from .forms import AdminUserRegisterForm, AdminUserUpdateForm


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
