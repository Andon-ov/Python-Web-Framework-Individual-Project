from django.contrib.auth import mixins as auth_mixin
from django.shortcuts import render, redirect
from django.views import generic as view
from django.views.generic.edit import FormMixin

from culinary_recipes.common.forms import RecipeCommentForm
from culinary_recipes.recipes_app.models import Recipe, BaseRecipe, Category, Ingredient, PreparationMethod


class AllCategoryListView(view.ListView):
    template_name = 'recipes/show-all-categories.html'
    model = Category


class BaseRecipeListView(auth_mixin.LoginRequiredMixin, view.ListView):
    paginate_by = 12

    template_name = 'recipes/show-all-base-recipes.html'
    model = BaseRecipe

    # for waiter
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('index')
        if request.user.profile.job_title == 'waiter':
            return redirect('index')
        return super().dispatch(request, *args, **kwargs)


# @cache_page(60*15)
def recipes_in_category(request, pk):
    category = Category.objects.filter(pk=pk).get()
    recipes = Recipe.objects.filter(category=category)

    context = {
        'category': category,
        'recipes': recipes,
    }
    return render(request, 'recipes/show-category-details.html', context)


class RecipeDetailsWaitersView(auth_mixin.LoginRequiredMixin, view.DetailView, FormMixin):
    template_name = 'recipes/recipe-details-waiters.html'
    model = Recipe
    form_class = RecipeCommentForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = RecipeCommentForm(initial={'post': self.object})
        return context


class RecipeDetailsView(auth_mixin.LoginRequiredMixin, view.DetailView, FormMixin):
    template_name = 'recipes/recipe-details.html'
    model = Recipe
    form_class = RecipeCommentForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = RecipeCommentForm(initial={'post': self.object})
        context['recipe_ingredients'] = Ingredient.objects.filter(recipe=self.kwargs['pk'])
        return context

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return self.handle_no_permission()
        if request.user.profile.job_title == 'waiter':
            recipe = kwargs.get('pk')
            return redirect('recipe detail waiters', pk=recipe)
        else:
            return super().dispatch(request, *args, **kwargs)


class BaseRecipeDetailsView(auth_mixin.LoginRequiredMixin, view.DetailView):
    template_name = 'recipes/base-details.html'
    model = BaseRecipe

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['prep_method'] = PreparationMethod.objects.filter(baserecipe=self.kwargs['pk'])
        return context


class SearchResultsView(view.ListView):
    model = Recipe
    template_name = 'recipes/culinary-search.html'

    def get_queryset(self):  # new
        queryset = super().get_queryset()
        pattern = self.__get_pattern()
        if pattern:
            queryset = queryset.filter(title__icontains=pattern)
        return queryset

    def __get_pattern(self):
        pattern = self.request.GET.get('pattern', None)
        return pattern.upper() if pattern else None
