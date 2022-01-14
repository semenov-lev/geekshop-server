from django.contrib.auth.views import LogoutView, LoginView
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import get_object_or_404
from django.views.generic import CreateView, UpdateView
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from authapp.forms import UserLoginForm, UserRegisterForm, UserProfileForm
from authapp.models import User
from baskets.models import Basket
from mainapp.mixin import UserDispatchMixin, BaseClassContextMixin


class UserLoginView(LoginView, BaseClassContextMixin):
    form_class = UserLoginForm
    template_name = 'authapp/login.html'
    title = 'GeekShop | Авторизация'


class UserRegisterView(CreateView, BaseClassContextMixin):
    model = User
    template_name = 'authapp/register.html'
    form_class = UserRegisterForm
    success_url = reverse_lazy('authapp:login')
    title = 'GeekShop | Регистрация'

    def form_valid(self, form):
        messages.success(self.request, 'Данные успешно обновлены!')
        super(UserRegisterView, self).form_valid(form)
        return HttpResponseRedirect(self.get_success_url())


class ProfileView(UpdateView, UserDispatchMixin, SuccessMessageMixin):
    model = User
    template_name = 'authapp/profile.html'
    form_class = UserProfileForm
    success_url = reverse_lazy('authapp:profile')

    def get_context_data(self, **kwargs):
        context = super(ProfileView, self).get_context_data(**kwargs)
        context['title'] = 'GeekShop | Профиль'
        context['baskets'] = Basket.objects.filter(user=self.request.user)
        return context

    def get_object(self, queryset=None):
        return get_object_or_404(User, pk=self.request.user.id)

    def form_valid(self, form):
        messages.success(self.request, 'Данные успешно обновлены!')
        super(ProfileView, self).form_valid(form)
        return HttpResponseRedirect(self.get_success_url())


class UserLogoutView(LogoutView):
    template_name = 'mainapp/index.html'
