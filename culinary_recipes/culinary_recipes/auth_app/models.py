from enum import Enum

from django.contrib.auth import models as auth_models
from django.core.validators import MinLengthValidator
from django.db import models

from culinary_recipes.auth_app.managers import AppUserManager


class AppUser(auth_models.AbstractBaseUser, auth_models.PermissionsMixin):
    email = models.EmailField(
        unique=True,
        null=False,
        blank=False,
    )
    date_joined = models.DateTimeField(
        auto_now_add=True,
    )
    is_staff = models.BooleanField(
        default=False,
        null=False,
        blank=False,
    )

    USERNAME_FIELD = 'email'

    objects = AppUserManager()


class ChoicesEnumMixin:
    @classmethod
    def choices(cls):
        return [(x.name, x.value) for x in cls]

    @classmethod
    def max_len(cls):
        return max(len(name) for name, _ in cls.choices())


class JobTitle(ChoicesEnumMixin, Enum):
    waiter = 'Waiter'
    cook = 'Cook'
    manager = 'Manager'


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
