from django.test import TestCase
from django.urls import reverse_lazy, reverse

from culinary_recipes.recipes_app.models import Recipe, Category, Menu, Photo, FoodPlate


class BaseTestCase(TestCase):
    def assertCollectionEmpty(self, collection, message=None):
        return self.assertEqual(0, len(collection), message)

    def assertCollectionNotEmpty(self, collection, message=None):
        return self.assertEqual(1, len(collection), message)



class recipes_in_category_view_tests(BaseTestCase):

    def test_recipe_add_one_recipe__expect_len_of_one(self):
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
        recipe.save()
        recipe.full_clean()

        response = self.client.get(reverse_lazy('category detail', kwargs={'pk': category.pk}))
        self.assertCollectionNotEmpty(response.context['recipes'])

    def test_recipe__expect_len_of_zero(self):
        menu = Menu.objects.create(
            title='alabala'
        )
        category = Category.objects.create(
            name='test',
            menu_id=menu.pk, )

        response = self.client.get(reverse('category detail', kwargs={'pk': category.pk}))

        self.assertCollectionEmpty(response.context['recipes'])
