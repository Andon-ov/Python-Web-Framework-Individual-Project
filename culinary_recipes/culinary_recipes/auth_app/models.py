from enum import Enum

from django.contrib.auth import models as auth_models
from django.contrib.auth.models import Group as BaseGroup
from django.core.validators import MinLengthValidator
from django.db import models

from culinary_recipes.auth_app.managers import AppUserManager
from culinary_recipes.core.mixins import ChoicesEnumMixin


class JobTitle(ChoicesEnumMixin, Enum):
    waiter = 'Сервитьор'
    cook = 'Готвач'
    manager = 'Мениджър'


class Profile(models.Model):
    FIRST_NAME_MIN_LENGTH = 3
    FIRST_NAME_MAX_LENGTH = 30

    LAST_NAME_MIN_LENGTH = 3
    LAST_NAME_MAX_LENGTH = 30

    first_name = models.CharField(
        max_length=FIRST_NAME_MAX_LENGTH,
        validators=(
            MinLengthValidator(FIRST_NAME_MIN_LENGTH),
        ),
        null=False,
        blank=False,
    )
    last_name = models.CharField(
        max_length=LAST_NAME_MAX_LENGTH,
        validators=(
            MinLengthValidator(LAST_NAME_MIN_LENGTH),
        ),
        null=False,
        blank=False,
    )

    job_title = models.CharField(
        verbose_name='Choice you job title',
        max_length=JobTitle.max_len(),
        choices=JobTitle.choices(),
        null=False,
        blank=False,
    )

    user = models.OneToOneField(
        'AppUser',
        primary_key=True,
        on_delete=models.CASCADE,
    )

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    def __str__(self):
        return self.user.email


class AppUser(auth_models.AbstractBaseUser, auth_models.PermissionsMixin):
    EMAIL_MAX_LENGTH = 255
    email = models.EmailField(
        verbose_name='email address',
        max_length=EMAIL_MAX_LENGTH,
        unique=True,
    )
    is_active = models.BooleanField(
        default=True
    )
    is_admin = models.BooleanField(
        default=False
    )
    is_staff = models.BooleanField(
        default=False
    )
    date_joined = models.DateTimeField(
        auto_now_add=True,
    )

    objects = AppUserManager()

    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.email
