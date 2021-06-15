import pytest

from amazon_price_tracker.products.scrapper import Scrapper


def test_scrapper_in_good_scenario():
    """
    Test that should return something
    """

    list_of_klocki_lego = Scrapper("Klocki Lego").get_list_of_products()

    assert len(list_of_klocki_lego) > 0
    assert list_of_klocki_lego is not None


def test_scrapper_in_bad_scenario():
    """
    In all cases Scrapper
    should return None
    """

    list_no_one = Scrapper("asdasdfdsfas dasfsdfsd asdasdas").get_list_of_products()

    list_no_two = Scrapper(
        "asdskdfhskjdhfkjsdhfkjshdfkjhsdkjfhsjk"
    ).get_list_of_products()

    list_no_three = Scrapper(
        "sdfkshdfjk ajfhsk jashdkjahsdu uhyasiudy"
    ).get_list_of_products()

    assert list_no_one == None
    assert list_no_two == None
    assert list_no_three == None
