import factory
import pytest
from faker import Faker

from amazon_price_tracker.products.models import Product, Tracker
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
        password="Fakee123!",
    )


@pytest.fixture
def user(db):
    """
    Returns user instance
    """
    return User.objects.create_user(
        email=faker.email(),
        password="Fakee123!",
    )


class UserFactory(factory.django.DjangoModelFactory):
    """
    Factory of User Model
    """

    email = faker.email()
    password = "argon2$argon2id$v=19$m=102400,t=2,p=8$MEpaa3JVdEJHVVZ4cFppa0ZlTWVaRQ$+xmq+D9nd6cAh003707S6Q"
    first_name = faker.first_name()
    last_name = faker.last_name()
    is_active = True
    is_staff = False
    is_superuser = False

    class Meta:
        model = User


class ProductFactory(factory.django.DjangoModelFactory):
    """
    Factory of Product Model
    """

    name = faker.slug()
    link = faker.url()
    image = faker.image_url()

    class Meta:
        model = Product


class TrackerFactory(factory.django.DjangoModelFactory):
    """
    Factory of Tracker Model
    """

    user = factory.SubFactory(UserFactory)
    product = factory.SubFactory(ProductFactory)
    price = 100

    class Meta:
        model = Tracker
