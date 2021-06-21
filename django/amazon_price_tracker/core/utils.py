import re

from django.utils.text import slugify


def is_password_valid_by_regex(password):
    """
    Check if given password
    match the REGEX
    """
    REGEX = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&#])[A-Za-z\d@$!%*?&#]{8,}$"
    if re.match(REGEX, password):
        return True
    return False


def slugify_pl(string):
    dictionary = {
        261: 97,  # ą
        263: 99,  # ć
        281: 101,  # ę
        322: 108,  # ł
        347: 115,  # ś
        243: 111,  # ó
        322: 108,  # ł
        324: 110,  # ń
        380: 122,  # ż
        378: 122,  # ź
    }

    return slugify(string.lower().translate(dictionary))
