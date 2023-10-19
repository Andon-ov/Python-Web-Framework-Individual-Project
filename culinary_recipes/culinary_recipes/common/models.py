from django.contrib.auth import get_user_model
from django.db import models

from culinary_recipes.recipes_app.models import Recipe

UserModel = get_user_model()


class RecipeComment(models.Model):
    text = models.TextField(
        null=False,
        blank=False,
        verbose_name='Your comment'
    )

    publication_date_and_time = models.DateTimeField(
        auto_now_add=True,
        blank=True,
        null=False,
    )

    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        null=False,
        blank=True,
    )

    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
        null=False,
        blank=True,
    )

    def __str__(self):
        return self.text

    class Meta:
        ordering = ('-id',)
