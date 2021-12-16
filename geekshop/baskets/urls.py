from django.urls import path
from .views import basked_add

app_name = 'baskets'

urlpatterns = [
    path('add/<int:id>/', basked_add, name='basked_add'),
]
