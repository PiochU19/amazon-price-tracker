from celery import shared_task

from amazon_price_tracker.account.utils import send_email_to_confirm_account
from amazon_price_tracker.period_task.utils import get_products_and_check_prices


@shared_task
def send_email_to_confirm_account_celery_task(user_pk):
    """
    Celery task which sends email
    """
    send_email_to_confirm_account(user_pk)


@shared_task
def check_price_periodic_celery_task():
    get_products_and_check_prices()
