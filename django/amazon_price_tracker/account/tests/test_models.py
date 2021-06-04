import pytest
from faker import Faker

from amazon_price_tracker.core.fixtures import admin, user
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError

User = get_user_model()
faker = Faker()


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


def test_password_should_fail_due_to_no_upper(db):
    try:
        User.objects.create_user(
            email=faker.email(),
            password="pasdasd12!",
        )
    except ValidationError as error:
        assert error.messages[0] == "Invalid password"


def test_password_should_fail_due_to_no_number(db):
    try:
        User.objects.create_user(
            email=faker.email(),
            password="Aasdafsd!!",
        )
    except ValidationError as error:
        assert error.messages[0] == "Invalid password"


def test_password_should_fail_due_to_no_special_character(db):
    try:
        User.objects.create_user(
            email=faker.email(),
            password="Asadasd12",
        )
    except ValidationError as error:
        assert error.messages[0] == "Invalid password"


def test_user_manager(admin, user):
    how_many_actives = User.objects.active().count()
    assert how_many_actives == 2

    User.objects.create_user(
        email=faker.email(),
        password="Afdssdf123!",
    )
    how_many_actives = User.objects.active().count()
    assert how_many_actives == 3

    User.objects.create_user(
        email=faker.email(),
        password="SAsadsdf123!",
        is_active=False,
    )
    how_many_actives = User.objects.active().count()
    assert how_many_actives == 3
