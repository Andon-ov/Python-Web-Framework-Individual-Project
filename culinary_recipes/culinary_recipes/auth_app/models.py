from enum import Enum

from django.contrib.auth import models as auth_models
from django.contrib.auth.models import AbstractBaseUser
from django.core.validators import MinLengthValidator
from django.db import models

from culinary_recipes.auth_app.managers import AppUserManager


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

    def __str__(self):
        return self.user.email


class AppUser(auth_models.AbstractBaseUser, auth_models.PermissionsMixin):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    # date_of_birth = models.DateField()
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = AppUserManager()

    USERNAME_FIELD = 'email'

    # REQUIRED_FIELDS = ['date_of_birth']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin
