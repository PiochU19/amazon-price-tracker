from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/account/", include("amazon_price_tracker.account.urls")),
    path("api/products/", include("amazon_price_tracker.products.urls")),
]
