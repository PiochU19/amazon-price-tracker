import os

from amazon_price_tracker.period_task.scrapper import Scrapper
from amazon_price_tracker.products.models import Product, Tracker
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags


def send_email_to_inform_about_low_price(email_to, first_name, link):
    """
    Email is sending if price provided by user is less than actual price
    """

    html_message = render_to_string(
        "price_went_below_email_template.html",
        {
            "link": link,
            "first_name": first_name,
        },
    )

    email_subject = "Price alert! Hurry up"
    text_content = strip_tags(html_message)
    email_from = os.environ.get("EMAIL_HOST_USER")

    email = EmailMultiAlternatives(
        email_subject,
        text_content,
        email_from,
        [email_to],
    )
    email.attach_alternative(html_message, "text/html")
    email.send()

    return True


def get_products_and_check_prices():
    """
    Function iterate through
    all Trackers and trigger
    function which sends alert
    about low price
    """

    products = Product.objects.all()

    for product in products:
        related_trackers = product.get_related_trackers()

        ## checks if at least one related tracker exist
        ## if not Product Model is deleted
        if related_trackers:
            actual_price = Scrapper(product.link).get_price()

            for tracker in related_trackers:

                ## if price provided by user is greater than actual price
                ## email function is trigerring
                ## and then tracker is deleted
                if actual_price < tracker.price:
                    send_email_to_inform_about_low_price(
                        tracker.user.email, tracker.user.first_name, product.link
                    )
                    tracker.delete()

        else:
            product.delete()
