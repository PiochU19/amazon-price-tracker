import re


def is_password_valid_by_regex(password):
    """
    Check if given password
    match the REGEX
    """
    REGEX = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&#])[A-Za-z\d@$!%*?&#]{8,}$"
    if re.match(REGEX, password):
        return True
    return False
