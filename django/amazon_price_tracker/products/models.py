import uuid

from amazon_price_tracker.core.models import CreatedModified
from amazon_price_tracker.core.utils import slugify_pl
from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.db.models.fields import UUIDField


class Product(CreatedModified):
    """
    Product is 'parent' Model
    for one Amazon Product
    """

    ## slug instead of id
    slug = models.SlugField(
        blank=True, unique=True, editable=False, primary_key=True, max_length=500
    )
    name = models.CharField(max_length=500)
    link = models.URLField(max_length=500)
    image = models.URLField(max_length=500)

    class Meta:
        ordering = ("-created",)
        verbose_name = "product"
        verbose_name_plural = "products"

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        """
        override save method
        """

        self.slug = slugify_pl(self.name)

        super(Product, self).save(*args, **kwargs)


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
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="trackers"
    )
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.IntegerField()

    class Meta:
        ordering = ("-created",)
        verbose_name = "tracker"
        verbose_name_plural = "trackers"

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name} -> {self.product.name}"
