import os

from amazon_price_tracker.account.tokens import token_generator_for_activate_account
from django.contrib.auth import get_user_model
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.html import strip_tags
from django.utils.http import urlsafe_base64_encode

User = get_user_model()


def send_email_to_confirm_account(user_pk):
    """
    Email is sending through
    celery during registration
    """

    user = User.objects.get(pk=user_pk)

    html_message = render_to_string(
        "account_confirmation_email.html",
        {
            "user": user,
            "upk": urlsafe_base64_encode(force_bytes(user.pk)),
            "token": token_generator_for_activate_account.make_token(user),
            "path": os.environ.get("PATH_SERVER"),
        },
    )
    email_subject = "Confirm your account"
    text_content = strip_tags(html_message)
    email_from = os.environ.get("EMAIL_HOST_USER")
    email_to = user.email

    email = EmailMultiAlternatives(
        email_subject,
        text_content,
        email_from,
        [email_to],
    )
    email.attach_alternative(html_message, "text/html")
    email.send()

    return True
