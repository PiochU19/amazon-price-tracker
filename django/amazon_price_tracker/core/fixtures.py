import pytest
from faker import Faker

from django.contrib.auth import get_user_model

User = get_user_model()
faker = Faker()


@pytest.fixture
def admin(db):
    """
    Returns superuser instance
    """
    return User.objects.create_superuser(
        email=faker.email(),
        password=faker.password(
            length=10,
            special_chars=True,
            digits=True,
            upper_case=True,
            lower_case=True,
        ),
    )


@pytest.fixture
def user(db):
    """
    Returns user instance
    """
    return User.objects.create_user(
        email=faker.email(),
        password=faker.password(
            length=10,
            special_chars=True,
            digits=True,
            upper_case=True,
            lower_case=True,
        ),
    )
