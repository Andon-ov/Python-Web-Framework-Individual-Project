from django.urls import path

from culinary_recipes.common.views import index, comment_recipe, comment_delete, comment_edite, standard

urlpatterns = (
    path('', index, name='index'),
    path('standard/', standard, name='standard'),
    path('comment/<int:recipe_id>/', comment_recipe, name='comment recipe'),
    path('comment/<int:recipe_id>/<int:pk>/edit/', comment_edite, name='comment edit'),
    path('comment/<int:recipe_id>/<int:pk>/delete/', comment_delete, name='comment delete'),
)
