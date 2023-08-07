from django.conf import settings
from django.urls import reverse

from culinary_recipes.recipes_app.models import Menu, Category, Photo, FoodPlate, Recipe
from tests.base_test_case import BestTestCase


class RecipeDetailsViewTests(BestTestCase):
    def test_get_details_view__when_anonymous_user__expect_to_redirect_to_login(self):
        menu = Menu.objects.create(
            title='alabala'
        )
        category = Category.objects.create(
            name='test',
            menu_id=menu.pk, )
        image = Photo.objects.create(
            name='test',
            image='test.jpg'
        )
        plate = FoodPlate(
            name='plate'
        )
        plate.save()
        recipe = Recipe.objects.create(
            title='Test',
            category=category,
            image_recipe=image,
            food_plate=plate
        )

        response = self.client.post(reverse('recipe detail', kwargs={'pk': recipe.pk}))
        expected_redirect_url = f"{settings.LOGIN_URL}?next={reverse('recipe detail', kwargs={'pk': recipe.pk})}"

        self.assertEqual(302, response.status_code)
        self.assertEqual(expected_redirect_url, response.headers.get('Location'))
