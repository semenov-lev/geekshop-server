from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from authapp.models import User
from .forms import AdminUserRegisterForm


def index(request):
    context = {
        'title': 'GeekShop - Администратор'
    }
    return render(request, 'admins/admin.html', context)


def user_read(request):
    context = {
        'title': 'GeekShop - Администратор | Пользователи',
        'all_users': User.objects.all()
    }
    return render(request, 'admins/admin-users-read.html', context)


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


def user_update(request, pk):
    context = {
        'user': pk
    }
    return render(request, 'admins/admin-users-update-delete.html', context)


def user_delete(request, pk):
    context = {
        'user': pk
    }
    return render(request, 'admins/admin-users-update-delete.html', context)
