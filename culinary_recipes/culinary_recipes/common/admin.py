from django.contrib import admin

from culinary_recipes.common.models import RecipeComment


@admin.register(RecipeComment)
class RecipeCommentAdmin(admin.ModelAdmin):
    list_display = ('recipe','text','user',)

