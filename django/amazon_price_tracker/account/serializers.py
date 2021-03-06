from rest_framework import serializers
from rest_framework.serializers import ValidationError

from amazon_price_tracker.account.celery_tasks import (
    send_email_to_confirm_account_celery_task,
)
from amazon_price_tracker.products.serializers import TrackerSerializer
from django.contrib.auth import get_user_model, password_validation
from django.core import exceptions
from django.db.models.fields import EmailField

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    password_confirmation = serializers.CharField(write_only=True)
    trackers = TrackerSerializer(read_only=True, many=True)

    class Meta:
        model = User
        fields = (
            "first_name",
            "last_name",
            "email",
            "password",
            "password_confirmation",
            "trackers",
        )
        extra_kwargs = {
            "password": {"write_only": True},
            "email": {"write_only": True},
            "last_name": {"write_only": True},
        }

    def create(self, data):
        """
        Override create method
        User Object 'create_user" method
        is called instead of normal create
        """

        user = User.objects.create_user(
            email=data["email"],
            first_name=data["first_name"],
            last_name=data["last_name"],
            password=data["password"],
            is_active=False,
        )

        send_email_to_confirm_account_celery_task.delay(user.pk)

        return user

    def validate(self, data):
        """
        Checks if two given password match
        """
        if data["password"] != data["password_confirmation"]:
            raise ValidationError({"password": "passwords don't match"})

        return data

    def validate_password(self, password):
        """
        Checks if password pass
        Password Validators
        """
        try:
            password_validation.validate_password(password=password)
        except exceptions.ValidationError:
            raise ValidationError("invalid password")

        return password
