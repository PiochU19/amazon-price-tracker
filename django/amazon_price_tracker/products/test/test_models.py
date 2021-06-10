import pytest

from pytest_factoryboy import register

from amazon_price_tracker.core.fixtures import ProductFactory, TrackerFactory


register(ProductFactory)
register(TrackerFactory)


def test_product_string_representation(db, product_factory):
    product = product_factory.create()

    assert f"{product}" == product.name


def test_tracker_string_representation(db, tracker_factory):
    tracker = tracker_factory.create()

    assert f"{tracker}" == f"{tracker.user.first_name} {tracker.user.last_name} -> {tracker.product.name}"
