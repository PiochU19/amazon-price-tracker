from django.core import exceptions
from rest_framework import serializers
from rest_framework.serializers import ValidationError

from django.contrib.auth import get_user_model, password_validation

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    password_confirmation = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = (
            "first_name",
            "last_name",
            "email",
            "password",
            "password_confirmation",
            "is_active",
            "is_staff",
        )
        extra_kwargs = {
            "password": {"write_only": True},
            "is_active": {"read_only": True},
            "is_staff": {"read_only": True},
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
