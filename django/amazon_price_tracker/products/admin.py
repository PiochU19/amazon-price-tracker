from amazon_price_tracker.products.models import Product, Tracker
from django.contrib import admin
from django.utils.translation import gettext_lazy as _


@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    """
    Product Model Custom Admin
    """

    model = Product
    fieldsets = (
        (
            _("Product"),
            {
                "fields": (
                    "name",
                    "link",
                    "image",
                )
            },
        ),
        (
            _("Dates"),
            {
                "fields": (
                    "created",
                    "modified",
                )
            },
        ),
    )
    readonly_fields = ("created", "modified")


@admin.register(Tracker)
class TrackerModelAdmin(admin.ModelAdmin):
    """
    Tracker Model Custom Admin
    """

    model = Tracker
    fieldsets = (
        (
            _("Foreign Keys"),
            {
                "fields": (
                    "user",
                    "product",
                )
            },
        ),
        (
            _("Price"),
            {"fields": ("price",)},
        ),
        (
            _("Dates"),
            {
                "fields": (
                    "created",
                    "modified",
                )
            },
        ),
    )
    readonly_fields = ("created", "modified")
    search_fields = ("user", "product")
    list_display = (
        "user",
        "product",
        "price",
    )
