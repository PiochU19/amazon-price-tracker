from django.urls import path
from rest_framework.routers import DefaultRouter
from amazon_price_tracker.account.views import UserViewSet


app_name = "account"


router = DefaultRouter()
router.register(r"user", UserViewSet)

urlpatterns = router.urls
