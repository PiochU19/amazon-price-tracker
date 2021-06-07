from rest_framework.routers import DefaultRouter

from amazon_price_tracker.account.views import (
    UserLoginAPIView,
    UserLogoutAPIView,
    UserViewSet,
)
from django.urls import path

app_name = "account"


urlpatterns = [
    path("login/", UserLoginAPIView.as_view(), name="login"),
    path("logout/", UserLogoutAPIView.as_view(), name="logout"),
]


router = DefaultRouter()
router.register(r"user", UserViewSet)

urlpatterns += router.urls
