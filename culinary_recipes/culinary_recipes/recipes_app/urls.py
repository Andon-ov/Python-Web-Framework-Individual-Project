from django.urls import path

from culinary_recipes.recipes_app.views import show_index

urlpatterns = (
    path('', show_index, name='index'),

)
