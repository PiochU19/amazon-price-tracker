import os
from celery import Celery
from celery.schedules import crontab
from django.conf import settings

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

app = Celery("amazon_price_tracker")

app.config_from_object("django.conf:settings", namespace="CELERY")


app.conf.beat_schedule = {
    "every-minute": {
        "task": "amazon_price_tracker.account.celery_tasks.check_price_periodic_celery_task",
        "schedule": crontab(hour=0, minute=0),
    }
}


app.autodiscover_tasks(settings.LOCAL_APPS)


@app.task(bind=True)
def debug_task(self):
    print(f"Request: {self.request!r}")
