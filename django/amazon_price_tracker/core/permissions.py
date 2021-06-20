from rest_framework.permissions import BasePermission


class IsObjectOwner(BasePermission):
    """
    Custom Permission Class
    Checks if authenticated user
    is owner of Object
    """

    def has_permission(self, request, view):
        """
        First we need to check
        if user is authenticated
        """

        return request.user and request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        """
        Then we need to check if
        authenticated user is Object
        """

        return obj.user == request.user
