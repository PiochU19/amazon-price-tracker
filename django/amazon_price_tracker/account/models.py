import datetime
import uuid

from amazon_price_tracker.core.utils import is_password_valid_by_regex
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from django.db import models
from django.utils.translation import gettext_lazy as _


class CustomUserManager(BaseUserManager):
    """
    Custom User Manager where user, and superuser is created
    based on email, not username.
    """

    def create_user(self, email, password, **extra_fields):

        if not is_password_valid_by_regex(password):
            raise ValidationError(_("Invalid password"))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, email, password, **extra_fields):

        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        return self.create_user(email, password, **extra_fields)

    def active(self):
        return self.filter(is_active=True)


class User(AbstractUser):
    """
    Custom User Model with
    email instead of username
    """

    uuid = models.UUIDField(
        unique=True, default=uuid.uuid4, editable=False, primary_key=True
    )
    email = models.EmailField(unique=True)
    username = None

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    class Meta:
        ordering = ("-date_joined",)
        verbose_name = "user"
        verbose_name_plural = "users"

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
