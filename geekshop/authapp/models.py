from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    image = models.ImageField(upload_to='users_images', blank=True)
    age = models.PositiveIntegerField(default=18)

    def __str__(self):
        return f'{self.username}'
