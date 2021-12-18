from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _


def validate_image(value):
    if value:
        if value.size > 5242880:
            raise ValidationError(_(f'Размер файла не может превышать 5 МБ'), params={'value': value})


def validate_age(value):
    if value < 1:
        raise ValidationError(_(f'Возраст не может быть меньше 1'), params={'value': value})
