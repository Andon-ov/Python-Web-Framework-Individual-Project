from django.urls import path

from culinary_recipes.common.views import index, comment_recipe, comment_delete, comment_edite

urlpatterns = (
    path('', index, name='index'),  # Show all actual manu

    # path('like/<int:photo_id>/', like_photo, name='like photo'),
    # path('share/<int:photo_id>/', share_photo, name='share photo'),
    path('comment/<int:recipe_id>/', comment_recipe, name='comment recipe'),
    path('comment/<int:recipe_id>/<int:pk>/edit/', comment_edite, name='comment edit'),
    path('comment/<int:recipe_id>/<int:pk>/delete/', comment_delete, name='comment delete'),
)
