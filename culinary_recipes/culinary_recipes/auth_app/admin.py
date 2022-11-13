from django.contrib import admin
# from django.contrib.auth import admin as auth_admin, get_user_model
#
# from culinary_recipes.auth_app.forms import SignUpForm
#
# UserModel = get_user_model()
#
#
# @admin.register(UserModel)
# class AppUserAdmin(auth_admin.UserAdmin):
#     ordering = ('email',)
#     list_display = ['email', 'last_login']
#     exclude = ['date_joined', ]
#     list_filter = ()
#     add_form = SignUpForm
#     add_fieldsets = (
#         (
#             None,
#             {
#                 "classes": ("wide",),
#                 "fields": ("email", "password1", "password2"),
#             },
#         ),
#         (
#             None,
#             {
#                 "classes": ("wide",),
#                 "fields": ("first_name", "last_name", "job_title"),
#             },
#         ),
#     )
from culinary_recipes.auth_app.models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    # inlines = (PetInlineAdmin,)
    list_display = ('first_name', 'last_name')