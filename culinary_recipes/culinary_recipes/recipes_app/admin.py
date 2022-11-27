from django.contrib import admin

from culinary_recipes.recipes_app.models import Category, PreparationMethod, Photo, Recipe, Ingredient, BaseRecipe, \
    Allergen, Menu, FoodPlate, Video, Food, Unit, BaseIngredient


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'order_index')


@admin.register(PreparationMethod)
class PreparationMethodAdmin(admin.ModelAdmin):
    pass


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    pass


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ('title', 'category',)
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
    list_display = (
        'recipe', 'food', 'amount_number', 'unit', 'quantity', 'preparation_method', 'base',
        'order_index')
    fields = (
        'recipe', 'last_recipe_edit', 'food', 'amount_number', 'unit', 'quantity', 'preparation_method', 'base',
        'order_index',
        'last_order_index')
    readonly_fields = ('last_order_index', 'last_recipe_edit')

    @staticmethod  # do i need it?
    def last_order_index(obj):
        latest_object = Ingredient.objects.values('order_index').last().get('order_index')
        return latest_object

    @staticmethod  # do i need it?
    def last_recipe_edit(obj):
        latest_object = Ingredient.objects.values('recipe__title').last().get('recipe__title')
        return latest_object


@admin.register(BaseRecipe)
class BaseRecipeAdmin(admin.ModelAdmin):
    list_display = ('title', 'base_type',)
    fieldsets = (
        (
            'First',
            {
                'fields': ('title', 'base_type', 'base_yield')
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
    ordering = ('name',)


@admin.register(Unit)
class UnitAdmin(admin.ModelAdmin):
    pass


@admin.register(BaseIngredient)
class BaseIngredientAdmin(admin.ModelAdmin):
    ordering = ('base', 'order_index')
    list_display = (
        'base', 'food', 'amount_number', 'unit', 'quantity', 'preparation_method', 'order_index',)
    fields = (
        'base', 'last_base_edit', 'food', 'amount_number', 'unit', 'quantity', 'preparation_method', 'order_index',
        'last_order_index')
    readonly_fields = ('last_order_index', 'last_base_edit',)

    @staticmethod  # do i need it?
    def last_order_index(obj):
        latest_object = BaseIngredient.objects.values('order_index').last().get('order_index')
        return latest_object

    @staticmethod  # do i need it?
    def last_base_edit(obj):
        latest_object = BaseIngredient.objects.last()
        return latest_object
