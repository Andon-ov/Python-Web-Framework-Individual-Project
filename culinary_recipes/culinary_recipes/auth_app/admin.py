from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from culinary_recipes.auth_app.models import Profile

UserModel = get_user_model()


class AppUserAdmin(UserAdmin):
    search_fields = ('email',)
    ordering = ('-date_joined',)
    list_display = (
        'email',
        'is_active',
        'is_admin',
        'is_staff',
        'is_superuser'
    )

    fieldsets = (
        (None, {
            'fields': (
                'email',
                'password',
            )}),
        (
            'Permissions',
            {'fields': (
                'is_active',
                'is_admin',
                'is_staff',
                'is_superuser',
                'groups',
                'user_permissions'
            )}),
    )
    add_fieldsets = (
        (None, {
            'classes': (
                'wide',
            ),
            'fields': (
                'email',
                'password1',
                'password2',
                'is_active',
                'is_admin',
                'is_staff',
                'is_superuser',
                'user_permissions',
                'groups',
            )}
         ),
    )


admin.site.register(UserModel, AppUserAdmin)


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name')
