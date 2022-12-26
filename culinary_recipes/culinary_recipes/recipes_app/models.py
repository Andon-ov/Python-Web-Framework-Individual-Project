from cloudinary import models as cloudinary_models
from django.db import models
from embed_video.fields import EmbedVideoField


class Menu(models.Model):
    TITLE_MAX_LENGTH = 120

    title = models.CharField(
        max_length=TITLE_MAX_LENGTH,
        blank=False,
        null=False
    )
    year = models.IntegerField(
        blank=True,
        null=True
    )
    summary = models.TextField(
        blank=True,
        null=True
    )
    order_index = models.PositiveIntegerField(
        null=True,
        blank=True
    )

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['order_index', 'id']


class Category(models.Model):
    NAME_MAX_LENGTH = 120
    NOTE_MAX_LENGTH = 120

    name = models.CharField(
        max_length=NAME_MAX_LENGTH,
        unique=True,
        blank=False,
        null=False
    )
    note = models.CharField(
        max_length=NOTE_MAX_LENGTH,
        null=True,
        blank=True
    )
    order_index = models.PositiveIntegerField(
        null=True,
        blank=True
    )
    is_activ = models.BooleanField(
        default=True,
        blank=False,
        null=False
    )

    # Many-to-one
    menu = models.ForeignKey(
        to='Menu',
        on_delete=models.CASCADE
    )
    image_category = models.ForeignKey(
        to='Photo',
        related_name='image_category',
        on_delete=models.RESTRICT,
        null=True,
        blank=True
    )

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['order_index', 'id']
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Recipe(models.Model):
    SPRING = 'spring'
    SUMMER = 'summer'
    AUTUMN = 'autumn'
    WINTER = 'winter'
    SEASONS_CHOICES = [(x, x) for x in (SPRING,
                                        SUMMER,
                                        AUTUMN,
                                        WINTER)]
    SEASONS_MAX_LENGTH = max(len(x) for x, _ in SEASONS_CHOICES)

    TITLE_MAX_LENGTH = 120
    SUMMARY_MAX_LENGTH = 500

    FINISH_MAX_LENGTH = 150

    PREPARATION_TIME_MAX_LENGTH = 100
    RELEASE_TIME_MAX_LENGTH = 100

    title = models.CharField(
        max_length=TITLE_MAX_LENGTH,
        unique=True,
        blank=False,
        null=False

    )
    summary = models.CharField(
        max_length=SUMMARY_MAX_LENGTH,
        blank=True,
        null=True,
        help_text='Summary for waiters!'
    )
    description = models.TextField(
        blank=True,
        null=True,
        help_text='How to prepare this recipe:'
    )
    finish = models.CharField(
        max_length=FINISH_MAX_LENGTH,
        blank=True,
        null=True,
        help_text='Final touches to the dish'
    )
    season = models.CharField(
        choices=SEASONS_CHOICES,
        max_length=SEASONS_MAX_LENGTH,
        blank=True,
        null=True,
    )
    preparation_time = models.CharField(
        max_length=PREPARATION_TIME_MAX_LENGTH,
        blank=True,
        null=True,
        help_text='Time needed to prepare the recipe'
    )
    release_time = models.CharField(
        max_length=RELEASE_TIME_MAX_LENGTH,
        blank=True,
        null=True,
        help_text='Release time from standard'
    )
    serving_value = models.IntegerField(
        null=True,
        blank=True,
        help_text='Serving size from menu:'
    )

    create_time = models.DateTimeField(
        auto_now_add=True
    )
    modify_time = models.DateTimeField(
        auto_now=True
    )
    order_index = models.PositiveIntegerField(
        null=True,
        blank=True
    )
    # Many-to-one
    video_recipe = models.ForeignKey(
        to='Video',
        related_name='video_recipe',
        on_delete=models.DO_NOTHING,
        blank=True,
        null=True
    )
    food_plate = models.ForeignKey(
        to='FoodPlate',
        on_delete=models.PROTECT
    )
    category = models.ForeignKey(
        to=Category,
        on_delete=models.CASCADE
    )

    preparation_method = models.ForeignKey(
        to='PreparationMethod',
        on_delete=models.PROTECT,
        null=True,
        blank=True
    )
    image_recipe = models.ForeignKey(
        to='Photo',
        related_name='image_recipe',
        on_delete=models.RESTRICT
    )

    allergen = models.ManyToManyField(
        to='Allergen',
        blank=True)

    def __str__(self):
        return f"{self.title}"

    class Meta:
        ordering = ['order_index', 'id']


class FoodPlate(models.Model):
    NAME_MAX_LENGTH = 50

    name = models.CharField(
        max_length=NAME_MAX_LENGTH,
        blank=False,
        null=False
    )

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class PreparationMethod(models.Model):
    NAME_MAX_LENGTH = 100

    name = models.CharField(
        max_length=NAME_MAX_LENGTH,
        blank=True,
        null=True
    )
    degree = models.IntegerField(
        blank=True,
        null=True
    )
    minute = models.IntegerField(
        blank=True,
        null=True
    )

    def __str__(self):
        if self.degree and self.minute:
            return f'{self.name} на {self.degree}°C за {self.minute} минути'
        if self.degree:
            return f'{self.name} на {self.degree}°C'
        if self.minute:
            return f'{self.name} за {self.minute} минути'

        else:
            return f'{self.name}'

    class Meta:
        ordering = ['name']


class Allergen(models.Model):
    TITLE_MAX_LENGTH = 100

    title = models.CharField(
        max_length=TITLE_MAX_LENGTH,
        blank=False,
        null=False,
    )

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('title',)


class Photo(models.Model):
    NAME_MAX_LENGTH = 200

    name = models.CharField(
        max_length=NAME_MAX_LENGTH,
        blank=False,
        null=False,
    )
    image = cloudinary_models.CloudinaryField(
        blank=False,
        null=False,
    )

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class Video(models.Model):
    NAME_MAX_LENGTH = 200

    name = models.CharField(
        max_length=NAME_MAX_LENGTH,
        blank=False,
        null=False,
    )
    video = EmbedVideoField()

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class Ingredient(models.Model):
    TITLE_MAX_LENGTH = 250
    QUANTITY_MAX_LENGTH = 50
    UNIT_MAX_LENGTH = 20

    amount_number = models.FloatField(
        null=True,
        blank=True,
        verbose_name='amount',
        help_text='What is the amount in "unit"?'
    )

    quantity = models.CharField(
        max_length=QUANTITY_MAX_LENGTH,
        null=True,
        blank=True,
        help_text='How many are there? If there are more than one, write it down:'

    )
    order_index = models.PositiveIntegerField(
        null=True,
        blank=True,
    )
    # Many-to-one

    recipe = models.ForeignKey(
        to='Recipe',
        on_delete=models.CASCADE,
        null=False,
        blank=False,
    )
    food = models.ForeignKey(
        to='Food',
        on_delete=models.PROTECT,
        null=False,
        blank=False,
    )
    unit = models.ForeignKey(
        to='Unit',
        on_delete=models.PROTECT,
        null=True,
        blank=True,
    )
    base = models.ForeignKey(
        to='BaseRecipe',
        related_name='base',
        on_delete=models.PROTECT,
        null=True,
        default=None,
        blank=True
    )
    preparation_method = models.ForeignKey(
        to='PreparationMethod',
        on_delete=models.PROTECT,
        null=True,
        blank=True,
    )

    def __str__(self):
        return f'{self.food}'

    class Meta:
        ordering = ['order_index', 'id', ]


class BaseRecipe(models.Model):
    TITLE_MAX_LENGTH = 100
    BASE_YIELD_MAX_LENGTH = 50

    BASE_TYPE_YIELD_MAX_LENGTH = 50
    NOTE_MAX_LENGTH = 200

    title = models.CharField(
        max_length=TITLE_MAX_LENGTH,
        blank=False,
        null=False,
        unique=True,
    )
    base_yield = models.CharField(
        max_length=BASE_YIELD_MAX_LENGTH,
        verbose_name='Yield',
        blank=True,
        null=True,
        help_text='The total weight of the base ingredients',
    )

    base_recipe_portions = models.IntegerField(
        blank=True,
        null=True,
        help_text='Amount of portions (people) the recipe is designed to serve'
    )
    base_type = models.CharField(
        max_length=BASE_YIELD_MAX_LENGTH,
        blank=True,
        null=True,
        help_text='Type of recipe: Base (Sauce, Dressing),Compound (Complete Dish),Batch (Large Volume Base Recipe),'
    )
    note = models.CharField(
        max_length=NOTE_MAX_LENGTH,
        blank=True,
        null=True,
    )
    preparation = models.TextField(
        blank=True,
        null=True,
    )
    # Many-to-many
    preparation_method = models.ManyToManyField(
        to='PreparationMethod',
        blank=True
    )
    allergen = models.ManyToManyField(
        to='Allergen',
        blank=True,
    )

    # photo
    # video
    def __str__(self):
        return f'{self.title} {self.id}'

    class Meta:
        ordering = ['title']


class Unit(models.Model):
    NAME_MAX_LENGTH = 60
    NAME_ABBREV_MAX_LENGTH = 60

    name = models.CharField(
        max_length=NAME_MAX_LENGTH,
        unique=True,
        null=False,
        blank=False,
    )
    name_abbrev = models.CharField(
        max_length=NAME_ABBREV_MAX_LENGTH,
        null=False,
        blank=True,
    )

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]


class Food(models.Model):
    NAME_MAX_LENGTH = 60

    name = models.CharField(
        max_length=NAME_MAX_LENGTH,
        blank=False,
        null=False,
        unique=True,
    )
    detail = models.TextField(
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]


class BaseIngredient(models.Model):
    TITLE_MAX_LENGTH = 250
    QUANTITY_MAX_LENGTH = 50
    UNIT_MAX_LENGTH = 20

    amount_number = models.FloatField(
        null=True,
        blank=True
    )

    quantity = models.CharField(
        max_length=QUANTITY_MAX_LENGTH,
        null=True,
        blank=True
    )
    order_index = models.PositiveIntegerField(
        null=True,
        blank=True
    )
    base = models.ForeignKey(
        to='BaseRecipe',
        on_delete=models.RESTRICT,
        blank=False,
        null=False
    )
    food = models.ForeignKey(
        to='Food',
        on_delete=models.PROTECT,
        null=False,
        blank=False
    )
    unit = models.ForeignKey(
        to='Unit',
        on_delete=models.PROTECT,
        null=True,
        blank=True,
    )

    preparation_method = models.ForeignKey(
        to='PreparationMethod',
        on_delete=models.PROTECT,
        null=True,
        blank=True,
    )

    def __str__(self):
        return f'{self.food} {self.amount_number} {self.unit}'

    class Meta:
        ordering = ('order_index', 'id',)
