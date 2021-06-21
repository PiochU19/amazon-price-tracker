import os


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
