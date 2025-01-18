from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import CustomUser
from core.models import *


@receiver(post_save, sender=CustomUser)
def create_user_cart_and_favorites(sender, instance, created, **kwargs):
    if created:
        Cart.objects.create(user=instance)
        Favorite.objects.create(user=instance)
