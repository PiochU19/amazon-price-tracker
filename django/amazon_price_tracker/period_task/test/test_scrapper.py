import pytest


from amazon_price_tracker.period_task.scrapper import Scrapper


def test_scrapper():
    """
    simple test that checks if Scrapper returns float type
    """

    should_be_float = Scrapper(
        "https://www.amazon.pl/Lego-75939-Laboratorium-Doktora-Dinozaur%C3%B3w/dp/B0813Q59TC/ref=sr_1_1?dchild=1&keywords=klocki+lego&qid=1624293560&sr=8-1"
    ).get_price()

    assert isinstance(should_be_float, float)
    assert should_be_float > 0
