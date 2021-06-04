from django.urls import path
from django.urls import path
from rest_framework.routers import DefaultRouter
from amazon_price_tracker.account.views import UserViewSet


router = DefaultRouter()
router.register(r"", UserViewSet)

urlpatterns = router.urls
