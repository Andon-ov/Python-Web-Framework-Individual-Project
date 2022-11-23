from django.urls import path, include

from culinary_recipes.recipes_app.views import RecipeDetailsView, BaseRecipeDetailsView, BaseRecipeListView, \
    SearchResultsView, RecipeDetailsWaitersView, AllCategoryListView, recipes_in_category

urlpatterns = (

    path('category/', AllCategoryListView.as_view(), name='all category'),  # Show all categories

    path('category/<int:pk>/', recipes_in_category, name='category detail'),  # Show all recipes in selected category

    path('base/', BaseRecipeListView.as_view(), name='base recipe'),  # Show all base recipes

    path('base/<int:pk>/', BaseRecipeDetailsView.as_view(), name='base_recipe detail'),  # Show selected base recipe

    path('detail/<int:pk>/', RecipeDetailsView.as_view(), name='recipe detail'),  # Show selected recipe

    path('detail-waiters/<int:pk>/', RecipeDetailsWaitersView.as_view(), name='recipe detail waiters'),
    # Show selected recipe waiters

    path("search/", SearchResultsView.as_view(), name="search"),  # Search

)
