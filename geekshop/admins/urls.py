from django.urls import path
from .views import index, user_create, user_read, user_update, user_delete

app_name = 'admins'

urlpatterns = [
    path('', index, name='index'),
    path('users/', user_read, name='user_read'),
    path('users-create/', user_create, name='user_create'),
    path('users-update/<int:pk>', user_update, name='user_update'),
    path('users-delete/<int:pk>', user_delete, name='user_delete'),
]
