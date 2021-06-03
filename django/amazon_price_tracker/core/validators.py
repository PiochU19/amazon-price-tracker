from amazon_price_tracker.core.utils import is_password_valid_by_regex
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


class RegexPasswordValidator:
    """
    Checks if there is:
    * special char
    * lowercase
    * uppercase
    * number
    """

    def validate(self, password, user=None):
        """
        Method where password is validated
        Password has to match the REGEX
        """

        if not is_password_valid_by_regex(password):
            raise ValidationError(
                _(
                    "This password must contain at least \
                    one uppercase, one lowercase, one \
                    number and one special character."
                )
            )

    def get_help_text(self):
        """
        Text below is displayed in
        User Creation Form e.g. Admin Panel
        """
        return _(
            "Your password must contain at least \
            one uppercase, one lowercase, one number \
            and one special character."
        )
