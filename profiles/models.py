from email.policy import default
from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _
import uuid


User = settings.AUTH_USER_MODEL


class Profile(models.Model):
    id = models.BigAutoField(primary_key=True, editable=False)
    pkid = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    country = models.CharField(
        verbose_name=_("Country"), max_length=200, default="Cameroon", null=True
    )
    city = models.CharField(
        verbose_name=_("City"), max_length=200, default="Bamenda", null=True
    )
    photo = models.ImageField(default="defautl_profile.png")
    is_married = models.BooleanField(default=False, verbose_name=_("Marital Status"))
    bio = models.TextField(verbose_name=_("About Yourselef"))
    proffession = models.CharField(
        verbose_name=_("What you do for a living"), max_length=255
    )
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username}'s profile"
