from django.urls import path
from authapp.views import UserLoginView, UserRegisterView, UserLogoutView, ProfileView

app_name = 'authapp'

urlpatterns = [
    path('login/', UserLoginView.as_view(), name='login'),
    path('register/', UserRegisterView.as_view(), name='register'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('verify/<str:email>/<str:activation_key>/', UserRegisterView.verify, name='verify'),
]
