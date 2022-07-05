from django.db.models.signals import post_save
from .models import Profile
from django.conf import settings
from django.dispatch import receiver
import logging
from rest_framework.authtoken.models import Token

logger = logging.getLogger(__name__)


User = settings.AUTH_USER_MODEL


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, *args, **kwargs):
    if created:
        Token.objects.create(user=instance)
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_profile(sender, instance, *args, **kwargs):
    instance.profile.save()
    logger.info(f"{instance}'s profile has been succsessfully created")
