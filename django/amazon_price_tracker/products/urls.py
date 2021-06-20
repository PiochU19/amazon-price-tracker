from rest_framework.routers import DefaultRouter

from amazon_price_tracker.products.views import ProductsListAPIView, TrackerViewSet
from django.urls import path

app_name = "products"


urlpatterns = [
    path("list/", ProductsListAPIView.as_view(), name="list_of_products"),
]


router = DefaultRouter()
router.register(r"tracker", TrackerViewSet)

urlpatterns += router.urls
