import pytest

from amazon_price_tracker.core.fixtures import user
from amazon_price_tracker.period_task.utils import get_products_and_check_prices
from amazon_price_tracker.products.models import Product, Tracker
from django.contrib.auth import get_user_model

User = get_user_model()


def test_get_products_and_check_prices(user):
    first_user = User.objects.all().first()
    product = Product.objects.create(
        name="Name",
        link="https://www.amazon.pl/Lego-75939-Laboratorium-Doktora-Dinozaur%C3%B3w/dp/B0813Q59TC/ref=sr_1_1?dchild=1&keywords=klocki+lego&qid=1624293560&sr=8-1",
        image="https://google.com/image",
    )
    Tracker.objects.create(product=product, user=first_user, price=9999)

    get_products_and_check_prices()

    assert Tracker.objects.all().count() == 0
    assert Product.objects.all().count() == 1

    get_products_and_check_prices()

    assert Product.objects.all().count() == 0
