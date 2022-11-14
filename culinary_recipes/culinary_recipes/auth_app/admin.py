from django.contrib import admin
from django.contrib.auth import models as auth_models, get_user_model
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from culinary_recipes.auth_app import forms as auth_forms
from culinary_recipes.auth_app.models import Profile

UserModel = get_user_model()


class UserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    form = auth_forms.UserChangeForm
    add_form = auth_forms.UserCreationForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('email', 'is_admin',)
    list_filter = ('is_admin',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Permissions', {'fields': ('is_admin',)}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()


# Now register the new UserAdmin...
admin.site.register(UserModel, UserAdmin)
# ... and, since we're not using Django's built-in permissions,
# unregister the Group model from admin.
admin.site.unregister(auth_models.Group)


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name')
