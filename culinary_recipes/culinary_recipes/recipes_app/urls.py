from django.urls import path, include

from culinary_recipes.recipes_app.views import create_recipe_view, CreateIngredientView, \
    RecipeDetailsView, BaseRecipeDetailsView, AllCategoryListView, menu_list_view, \
    category_list_view, BaseRecipeListView, SearchResultsView, RecipeDetailsWaitersView

urlpatterns = (

    path('menu/<int:pk>/', menu_list_view, name='menu list'),  # Show categories in selected menu

    path('category/', AllCategoryListView.as_view(), name='all category'),  # Show all categories

    path('category/<int:pk>/', category_list_view, name='category detail'),  # Show all recipes in selected category

    path('base/', BaseRecipeListView.as_view(), name='base recipe'),  # Show all base recipes

    path('base/<int:pk>/', BaseRecipeDetailsView.as_view(), name='base_recipe detail'),  # Show selected base recipe

    path('detail/<int:pk>/', RecipeDetailsView.as_view(), name='recipe detail'),  # Show selected recipe

    path('detail-waiters/<int:pk>/', RecipeDetailsWaitersView.as_view(), name='recipe detail waiters'),
    # Show selected recipe waiters

    path("search/", SearchResultsView.as_view(), name="search"),  # Search

    path('create/', include(
        [path('recipe/', create_recipe_view, name='create recipe'),
         # path('ingredient/', create_ingredient_view, name='create ingredient'),
         path('ingredient/', CreateIngredientView.as_view(), name='create ingredient'),
         ])))
