from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model

User = get_user_model()


@admin.register(User)
class UserAdminModel(UserAdmin):
    """
    Custom User Model Admin
    """

    model = User
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "email",
                    "password",
                )
            },
        ),
        (
            _("Personal Info"),
            {
                "fields": (
                    "first_name",
                    "last_name",
                )
            },
        ),
        (
            _("Permission"),
            {
                "fields": (
                    "is_active",
                    "is_superuser",
                )
            },
        ),
        (
            _("Dates"),
            {
                "fields": (
                    "date_joined",
                    "last_login",
                )
            },
        ),
    )
    list_display = (
        "email",
        "first_name",
        "last_name",
        "is_active",
    )
    search_fields = ("first_name",)
    readonly_fields = (
        "id",
        "date_joined",
        "last_login",
    )
    list_filter = ()
    filter_horizontal = ()
    ordering = ("-date_joined",)
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "email",
                    "password1",
                    "password2",
                    "first_name",
                    "last_name",
                    "is_staff",
                    "is_active",
                ),
            },
        ),
    )
