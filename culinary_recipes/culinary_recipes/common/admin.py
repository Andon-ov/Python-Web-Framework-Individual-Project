from django.contrib import admin

from culinary_recipes.common.models import RecipeComment, HomePage


@admin.register(RecipeComment)
class RecipeCommentAdmin(admin.ModelAdmin):
    pass


@admin.register(HomePage)
class HomePageAdmin(admin.ModelAdmin):
    pass
