from rest_framework.routers import DefaultRouter

from amazon_price_tracker.account.views import (
    UserAccountActivateView,
    UserLoginAPIView,
    UserLogoutAPIView,
    UserViewSet,
)
from django.urls import path

app_name = "account"


urlpatterns = [
    path("login/", UserLoginAPIView.as_view(), name="login"),
    path("logout/", UserLogoutAPIView.as_view(), name="logout"),
    path(
        "activate/<upkb64>/<token>",
        UserAccountActivateView.as_view(),
        name="account_confirmation",
    ),
]


router = DefaultRouter()
router.register(r"user", UserViewSet)

urlpatterns += router.urls
