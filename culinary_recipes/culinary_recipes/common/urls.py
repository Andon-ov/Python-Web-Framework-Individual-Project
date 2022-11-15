from django.urls import path

from culinary_recipes.common.views import index, comment_recipe

urlpatterns = (
    path('', index, name='index'),  # Show all actual manu

    # path('like/<int:photo_id>/', like_photo, name='like photo'),
    # path('share/<int:photo_id>/', share_photo, name='share photo'),
    path('comment/<int:recipe_id>/', comment_recipe, name='comment recipe'),
)
