from django.contrib.auth.models import BaseUserManager
from django.utils.translation import gettext_lazy as _
from django.core.validators import validate_email
from django.core.exceptions import ValidationError


class CustomUserManager(BaseUserManager):
    def validate_email(self, email):
        try:
            validate_email(email)
        except ValidationError:
            raise ValueError("You must provide a valide email.")

    def create_user(
        self, username, first_name, last_name, email, password, **extra_fields
    ):

        if not username:
            raise ValueError(_("User must provide a username."))

        if not first_name:
            raise ValueError(_("User must provide First Name"))

        if not last_name:
            raise ValueError(_("User must provide Last Name."))

        if email:
            email = self.normalize_email(email)
            self.validate_email(email)
        else:
            raise ValueError("Base User Account must have an email address")

        user = self.model(
            username=username,
            first_name=first_name,
            last_name=last_name,
            email=email,
            **extra_fields
        )

        user.set_password(password)
        user.extra_fields.setdefault("is_superuser", False)
        user.extra_fields.setdefault("is_staff", False)

        user.save(using=self._db)

        return user

    def create_superuser(
        self, username, first_name, last_name, password, email, **extra_fields
    ):

        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_superuser") is not True:
            raise ValueError("For a superuser account you must have 'superuser=True'")

        if extra_fields.get("is_staff") is not True:
            raise ValueError("For a superuser account you must have 'is_staff=True'")

        if extra_fields.get("is_active") is not True:
            raise ValueError("For a superuser accoutn you must have 'is_active=True'")

        if not username:
            raise ValueError(_("Username not provided."))

        if not first_name:
            raise ValueError(_("First Name not provided."))

        if not last_name:
            raise ValueError(_("Last Name not provided."))

        if email:
            email = self.normalize_email(email)
            self.validate_email(email)
        else:
            raise ValueError(_("Email address not provided."))

        user = self.model(
            username=username,
            email=email,
            first_name=first_name,
            last_name=last_name,
            **extra_fields
        )

        user.set_password(password)
        user.save(using=self._db)
        return user
