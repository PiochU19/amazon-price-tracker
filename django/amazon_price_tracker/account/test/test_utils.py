import pytest

from amazon_price_tracker.account.utils import send_email_to_confirm_account
from amazon_price_tracker.core.fixtures import user


def test_email_sending(user):
    pk = user.pk
    assert send_email_to_confirm_account(pk)
