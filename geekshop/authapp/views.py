from django.conf import settings
from django.contrib.auth.views import LogoutView, LoginView
from django.contrib.messages.views import SuccessMessageMixin
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404, render
from django.views.generic import CreateView, UpdateView
from django.contrib import messages, auth
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, reverse
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
        messages.success(self.request,
                         'Регистрация прошла успешно!\nДля завершения регистрации, пройдите по ссылке в сообщении, '
                         'которое должно прийти на указанную вами электронную почту')
        super(UserRegisterView, self).form_valid(form)
        user = self.object
        self.send_verify_link(user)
        return HttpResponseRedirect(self.get_success_url())

    def send_verify_link(self, user):
        verify_link = reverse('authapp:verify', args=[user.email, user.activation_key])
        subject = f'Для активации учетной записи {user.username}, пройдите по ссылке'
        message = f'Для подтверждения учетной заприси {user.username}, на портале\n{settings.DOMAIN_NAME}{verify_link}'
        return send_mail(subject, message, settings.EMAIL_HOST_USER, [user.email], fail_silently=False)

    def verify(self, email, activation_key):
        try:
            user = User.objects.get(email=email)
            if user and user.activation_key == activation_key and not user.is_activation_key_expires():
                user.activation_key = ''
                user.activation_key_expires = None
                user.is_active = True
                user.save()
                auth.login(self, user)
            return render(self, 'authapp/verification.html')
        except Exception:
            return HttpResponseRedirect(reverse('index'))


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
