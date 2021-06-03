from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _


class SpecialCharValidator:
    """
    Checks if there is a special
    char in password
    """

    def validate(self, password, user=None):
        """
        Method where password is validated
        """
        if not any(letter in "!@#$%^&*()-+?_=,<>/" for letter in password):
            raise ValidationError(
                _("This password must contain at least one special chararcter.")
            )

    def get_help_text(self):
        return _("Your password must contain at least one special character.")
