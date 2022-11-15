from django.urls import reverse
from django.views.generic.edit import FormMixin

from culinary_recipes.common.forms import RecipeCommentForm
from culinary_recipes.recipes_app.forms import RecipeCreateForm, IngredientCreateForm
from culinary_recipes.recipes_app.models import Recipe, BaseRecipe, Category, Menu, Ingredient, PreparationMethod
from django.contrib.auth import mixins as auth_mixin
from django.shortcuts import render, redirect
from django.views import generic as view


# show all categories
class AllCategoryListView(view.ListView):
    template_name = 'recipes/show-all-categories.html'
    model = Category


# show all base recipe

class BaseRecipeListView(auth_mixin.LoginRequiredMixin, view.ListView):
    paginate_by = 12

    template_name = 'recipes/show-all-base-recipes.html'
    model = BaseRecipe

    # for waiter
    def dispatch(self, request, *args, **kwargs):
        if request.user.profile.job_title == 'waiter':
            print(request)
            return redirect('index')
        return super().dispatch(request, *args, **kwargs)


# show menu -> categories
def menu_list_view(request, pk):
    menu = Menu.objects.filter(pk=pk).get()
    categories = Category.objects.filter(menu_id=menu)
    context = {
        'menu': menu,
        'categories': categories,
    }
    return render(request, 'recipes/menu-categories-list.html', context)


# show recipes in category
def category_list_view(request, pk):
    category = Category.objects.filter(pk=pk).get()
    recipes = Recipe.objects.filter(category_id=category)
    context = {
        'category': category,
        'recipes': recipes,
    }
    return render(request, 'recipes/show-category-details.html', context)


def create_recipe_view(request):
    if request.method == 'POST':
        form = RecipeCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = RecipeCreateForm()
        context = {
            'form': form
        }
        return render(request, 'recipes/create-recipe.html', context)


class CreateIngredientView(view.FormView):
    template_name = 'recipes/create-ingredient.html'
    form_class = IngredientCreateForm
    success_url = '/create/ingredient/'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class RecipeDetailsWaitersView(auth_mixin.LoginRequiredMixin, view.DetailView):
    template_name = 'recipes/recipe-details-waiters.html'
    model = Recipe


# show recipes


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
        if request.user.profile.job_title == 'waiter':
            recipe = kwargs.get('pk')
            return redirect('recipe detail waiters', pk=recipe)
        else:
            return super().dispatch(request, *args, **kwargs)


# show base recipe
class BaseRecipeDetailsView(auth_mixin.LoginRequiredMixin, view.DetailView):
    template_name = 'recipes/base-details.html'
    model = BaseRecipe

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['recipe_ingredients'] = Ingredient.objects.filter(recipe=self.kwargs['pk'])
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
