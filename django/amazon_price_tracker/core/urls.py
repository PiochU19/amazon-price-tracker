import os

from drf_yasg import openapi, views
from rest_framework import permissions

from django.urls import path

app_name = "core"


# Setting Swagger schema view
schema_view = views.get_schema_view(
    openapi.Info(
        title="API Documentation",
        description="Amazon Price Tracker API Documentation",
        default_version=str(os.environ.get("VERSION")),
    ),
    public=True,
    permission_classes=[
        permissions.AllowAny,
    ],
)


urlpatterns = [
    path("", schema_view.with_ui("swagger", cache_timeout=0), name="swagger"),
]
