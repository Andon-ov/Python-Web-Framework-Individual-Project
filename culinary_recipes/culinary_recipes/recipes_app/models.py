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
    summary = models.CharField(
        max_length=200,
        blank=True,
        null=True
    )
    order_index = models.PositiveIntegerField(
        null=True,
        blank=True
    )

    # sort by custom index

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['order_index']


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

    # Many-to-one
    menu = models.ForeignKey(
        to='Menu',
        on_delete=models.DO_NOTHING
    )
    image_category = models.ForeignKey(
        to='Photo',
        related_name='image_category',
        on_delete=models.DO_NOTHING,
        null=True,
        blank=True
    )

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['order_index', ]
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
        help_text='Serving size from menu'
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
        on_delete=models.PROTECT
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
        on_delete=models.DO_NOTHING
    )
    #  Many-to-many
    ingredient = models.ManyToManyField(
        to='Ingredient',
        blank=True
    )
    allergen = models.ManyToManyField(
        to='Allergen',
        blank=True)

    def get_ingredients(self):
        return ", ".join(sorted([str(i.title) for i in self.ingredient.all()]))

    def get_allergens(self):
        return ", ".join([str(i) for i in self.allergen.all()])

    def __str__(self):
        return f"{self.title} {self.get_ingredients()}"

    class Meta:
        ordering = ['order_index', ]


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
    DEGREE_MAX_LENGTH = 100
    MINUTE_MAX_LENGTH = 100

    name = models.CharField(
        max_length=NAME_MAX_LENGTH,
        blank=True,
        null=True
    )
    degree = models.CharField(
        max_length=DEGREE_MAX_LENGTH,
        blank=True,
        null=True
    )
    minute = models.CharField(
        max_length=MINUTE_MAX_LENGTH,
        blank=True,
        null=True
    )

    def __str__(self):
        return f'{self.name} {self.degree} {self.minute}'

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
    image = models.ImageField(
        upload_to='images'
    )

    # image = models.URLField()

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

    title = models.CharField(
        max_length=TITLE_MAX_LENGTH,
        blank=False,
        null=False,
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
    unit = models.CharField(
        max_length=UNIT_MAX_LENGTH,
        default='грама',
        null=True,
        blank=True
    )
    # Many-to-one
    amount_number = models.ForeignKey(
        to='Amount',
        blank=True,
        null=True,
        on_delete=models.RESTRICT,
        related_name='amount_number'
    )

    base = models.ForeignKey(
        to='BaseRecipe',
        related_name='base',
        on_delete=models.DO_NOTHING,
        null=True,
        default=None,
        blank=True
    )
    preparation_method = models.ForeignKey(
        to='PreparationMethod',
        null=True,
        blank=True,
        on_delete=models.PROTECT
    )

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['order_index', 'id', 'title']


class BaseRecipe(models.Model):
    TITLE_MAX_LENGTH = 100
    BASE_YIELD_MAX_LENGTH = 50

    BASE_TYPE_YIELD_MAX_LENGTH = 50
    NOTE_MAX_LENGTH = 200

    title = models.CharField(
        max_length=TITLE_MAX_LENGTH,
        blank=False,
        null=False,
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
    ingredient = models.ManyToManyField(
        to='Ingredient',
        blank=True
    )
    allergen = models.ManyToManyField(
        to='Allergen',
        blank=True
    )

    # photo
    # video
    def __str__(self):
        return f'{self.id} {self.title}'

    def get_ingredients(self):
        return ", ".join([f'{i.title} {i.amount_number} {i.unit}' for i in self.ingredient.all()])

    def get_allergens(self):
        return ", ".join([str(i) for i in self.allergen.all()])

    class Meta:
        ordering = ['title']


class Amount(models.Model):
    number = models.PositiveIntegerField(
        blank=True,
        null=True,
    )

    def __str__(self):
        return f'{self.number}'

    class Meta:
        ordering = ['number']
