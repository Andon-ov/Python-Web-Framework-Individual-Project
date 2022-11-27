from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from culinary_recipes.common.forms import RecipeCommentForm, RecipeCommentDeleteForm, RecipeCommentEditForm
from culinary_recipes.common.models import RecipeComment
from culinary_recipes.recipes_app.models import Recipe

UserModel = get_user_model()


def index(request):
    context = {
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


def comment_edite(request, pk, recipe_id):
    recipe = Recipe.objects.filter(pk=recipe_id).get()
    comment = RecipeComment.objects.filter(pk=pk).get()
    if request.method == 'POST':
        form = RecipeCommentEditForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            return redirect('recipe detail', pk=recipe.pk)
    else:
        form = RecipeCommentEditForm(instance=comment)
    context = {
        'form': form,
        'comment': comment,
        'recipe': recipe
    }
    return render(request, 'comment/comment-edit-page.html', context)


def comment_delete(request, pk, recipe_id):
    recipe = Recipe.objects.filter(pk=recipe_id).get()
    comment = RecipeComment.objects.filter(pk=pk).get()
    if request.method == 'POST':
        form = RecipeCommentDeleteForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            return redirect('recipe detail', pk=recipe.pk)
    else:
        form = RecipeCommentDeleteForm(instance=comment)
    context = {
        'form': form,
        'comment': comment,
        'recipe': recipe
    }
    return render(request, 'comment/comment-delete-page.html', context)
