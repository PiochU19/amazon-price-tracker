import uuid

from amazon_price_tracker.core.models import CreatedModified
from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.db.models.fields import UUIDField


class Product(CreatedModified):
    """
    Product is 'parent' Model
    for one Amazon Product
    """

    ## UUID instead of id to prevent danger
    uuid = models.UUIDField(
        unique=True, default=uuid.uuid4, editable=False, primary_key=True
    )
    name = models.CharField(max_length=100)
    link = models.URLField(max_length=255)
    image = models.URLField(max_length=255)

    class Meta:
        ordering = ("-created",)
        verbose_name = "product"
        verbose_name_plural = "products"

    def __str__(self):
        return self.name


class Tracker(CreatedModified):
    """
    Link Model between User and Product
    with additional 'price' field
    Price is specified by User
    """

    ## UUID instead of id to prevent danger
    uuid = models.UUIDField(
        unique=True, default=uuid.uuid4, editable=False, primary_key=True
    )
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.IntegerField()

    class Meta:
        ordering = ("-created",)
        verbose_name = "tracker"
        verbose_name_plural = "trackers"

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name} -> {self.product.name}"
