import pytest

from amazon_price_tracker.core.utils import is_password_valid_by_regex


def test_is_password_valid_by_regex_should_pass():
    """
    Passwords do match the REGEX
    """
    password = "Password123!"
    assert is_password_valid_by_regex(password)

    password = "Givemeajobplz999?"
    assert is_password_valid_by_regex(password)


def test_is_password_valid_by_regex_should_fail():
    """
    Passwords don't match the REGEX
    """
    password = "noupperhere1!"
    assert not is_password_valid_by_regex(password)

    password = "NOLOWERHERE1!"
    assert not is_password_valid_by_regex(password)

    password = "Nonumberhere!"
    assert not is_password_valid_by_regex(password)

    password = "Nospecialchar1"
    assert not is_password_valid_by_regex(password)
