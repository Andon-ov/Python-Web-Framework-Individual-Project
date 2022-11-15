from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from culinary_recipes.common.forms import RecipeCommentForm
from culinary_recipes.recipes_app.models import Menu, Category, Recipe

UserModel = get_user_model()


def index(request):
    menus = Menu.objects.all()
    categories = Category.objects.all()
    context = {
        'menus': menus,
        'categories': categories,
    }
    return render(request, 'index.html', context)


@login_required
def comment_recipe(request, recipe_id):
    recipe = Recipe.objects.filter(pk=recipe_id).get()
    user = UserModel.objects.filter(pk=request.user.pk).get()

    form = RecipeCommentForm(request.POST)

    if form.is_valid():
        comment = form.save(commit=False)
        comment.recipe = recipe
        comment.user = user
        comment.save()

    return redirect("recipe detail", pk=recipe.id)
