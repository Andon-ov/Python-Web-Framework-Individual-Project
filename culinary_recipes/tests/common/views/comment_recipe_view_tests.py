# from datetime import datetime
#
# from django.contrib.auth import get_user_model
# from django.test import TestCase
# from django.urls import reverse
#
# from culinary_recipes.common.models import RecipeComment
# from culinary_recipes.recipes_app.models import Menu, Category, Photo, FoodPlate, Recipe
#
# UserModel = get_user_model()
#
#
# class CommentRecipeTest(TestCase):
#     VALID_USER_DATA = {
#         'email': 'test@mail.com',
#         'password': 'pass',
#         'date_joined': datetime.now(),
#         'is_admin': True
#     }
#
#     def test_comment_recipe_view__add_comment(self):
#         user = UserModel.objects.create_user(**self.VALID_USER_DATA)
#         self.client.login(**self.VALID_USER_DATA)
#
#         menu = Menu.objects.create(
#             title='alabala'
#         )
#         category = Category.objects.create(
#             name='test',
#             menu_id=menu.pk, )
#         image = Photo.objects.create(
#             name='test',
#             image='test.jpg'
#         )
#         plate = FoodPlate(
#             name='plate'
#         )
#         plate.save()
#         recipe = Recipe.objects.create(
#             title='Test',
#             category=category,
#             image_recipe=image,
#             food_plate=plate
#         )
#
#         comment = RecipeComment.objects.create(
#             text='This is a comment'
#         )
#         recipe.save()
#         recipe.full_clean()
#
#         response = self.client.put(reverse('comment recipe', comment, recipe.pk, user.pk))
#         print(response)
#         # self.assertCollectionNotEmpty(response.context['recipes'])
