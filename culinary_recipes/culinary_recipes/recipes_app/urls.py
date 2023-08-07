from django.urls import path

from culinary_recipes.recipes_app.views import RecipeDetailsView, BaseRecipeDetailsView, BaseRecipeListView, \
    SearchResultsView, RecipeDetailsWaitersView, AllCategoryListView, recipes_in_category

urlpatterns = (
    # Show all categories
    path('category/', AllCategoryListView.as_view(), name='all category'),
    # Show all recipes in selected category
    path('category/<int:pk>/', recipes_in_category, name='category detail'),
    # Show all base recipes
    path('base/', BaseRecipeListView.as_view(), name='base recipe'),
    # Show selected base recipe
    path('base/<int:pk>/', BaseRecipeDetailsView.as_view(), name='base_recipe detail'),
    # Show selected recipe
    path('detail/<int:pk>/', RecipeDetailsView.as_view(), name='recipe detail'),
    # Show selected recipe waiters
    path('detail-waiters/<int:pk>/', RecipeDetailsWaitersView.as_view(), name='recipe detail waiters'),
    # Search
    path("search/", SearchResultsView.as_view(), name="search"),
)
