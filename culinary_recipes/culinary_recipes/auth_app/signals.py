from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver

from culinary_recipes.auth_app.models import Profile

UserModel = get_user_model()


@receiver(signal=post_save, sender=UserModel)
def create_empty_profile(instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
