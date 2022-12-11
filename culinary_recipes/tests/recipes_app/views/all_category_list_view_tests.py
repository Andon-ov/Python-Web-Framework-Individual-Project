from django.test import TestCase
from django.urls import reverse

from culinary_recipes.recipes_app.models import Category, Menu


class BaseTestCase(TestCase):
    def assertCollectionEmpty(self, collection, message=None):
        return self.assertEqual(0, len(collection), message)

    def assertCollectionNotEmpty(self, collection, message=None):
        return self.assertEqual(1, len(collection), message)


class AllCategoryListViewTests(BaseTestCase):
    def test_all_category_list_view__when_no_category__expect_empty_message(self):
        response = self.client.get(reverse('all category'))

        self.assertCollectionEmpty(response.context['category_list'])

    def test_all_category_list_view__when_category__expect_one_category(self):
        menu = Menu.objects.create(
            title='alabala'
        )
        Category.objects.create(
            name='test',
            menu_id=menu.pk, )

        response = self.client.get(reverse('all category'))

        self.assertCollectionNotEmpty(response.context['category_list'])
