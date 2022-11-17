from culinary_recipes.recipes_app.models import Category, PreparationMethod, Photo, Recipe, Ingredient, BaseRecipe, \
    Allergen, Menu, FoodPlate, Video, Food, Unit, BaseIngredient
from django.contrib import admin


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(PreparationMethod)
class PreparationMethodAdmin(admin.ModelAdmin):
    pass


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    pass


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', ) #'get_ingredients',
    list_filter = ('title',)
    search_fields = ('title',)
    fieldsets = (
        (
            'Main',
            {
                'fields': (
                    'title', 'category', 'image_recipe', 'food_plate', 'description', 'finish',
                    'preparation_method', 'preparation_time')
            }
        ),
        (
            'Waiters',
            {
                'fields': ('summary', 'allergen', 'serving_value', 'release_time')
            }
        ),
        (
            'Last',
            {
                'fields': ('video_recipe', 'season',)
            }
        ),
    )


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    pass


@admin.register(BaseRecipe)
class BaseRecipeAdmin(admin.ModelAdmin):
    fieldsets = (
        (
            'First',
            {
                'fields': ('title', 'base_type', 'ingredient', 'base_yield')
            }
        ),
        (
            'Second',
            {
                'fields': ('note', 'preparation', 'preparation_method', 'allergen', 'base_recipe_portions')
            }
        ),
    )


@admin.register(Allergen)
class AllergensAdmin(admin.ModelAdmin):
    pass


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    pass


@admin.register(FoodPlate)
class FoodPlateAdmin(admin.ModelAdmin):
    pass


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    pass


@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    pass

@admin.register(Unit)
class UnitAdmin(admin.ModelAdmin):
    pass

@admin.register(BaseIngredient)
class BaseIngredientAdmin(admin.ModelAdmin):
    pass