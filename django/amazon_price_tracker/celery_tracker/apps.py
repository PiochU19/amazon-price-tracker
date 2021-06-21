from django.apps import AppConfig


class CeleryTrackerConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "amazon_price_tracker.celery_tracker"
