import pytest

from amazon_price_tracker.core.fixtures import admin, user


def test_admin(admin):
    """
    Test if superuser
    is created correctly
    """

    assert admin.is_superuser
    assert admin.is_staff
    assert admin.is_active


def test_user(user):
    """
    Test if user is
    created correctly
    """

    assert not user.is_superuser
    assert not user.is_staff
    assert user.is_active
