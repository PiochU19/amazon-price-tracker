from django.urls import path
from amazon_price_tracker.products.views import ProductsListAPIView


app_name = "products"


urlpatterns = [
    path("list/", ProductsListAPIView.as_view(), name="list_of_products"),
]
