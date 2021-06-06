from django.shortcuts import redirect
from rest_framework import (
    viewsets,
    mixins,
    status,
    permissions,
)
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from amazon_price_tracker.account.serializers import UserSerializer

User = get_user_model()


class UserViewSet(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet,
):
    """
    User Model View Set with two methods
    POST for registration
    GET for retrieving data
    """

    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_object(self):
        """
        GET method always returns
        logged in User
        """
        return self.request.user

    def list(self, request):
        """
        This allows us to retrieve
        user data, by making GET request
        without provided primary key
        """
        return self.retrieve(request, pk=request.user.pk)

    def get_permissions(self):
        if self.request.method == "POST":
            self.permission_classes = [permissions.AllowAny]

        return super(UserViewSet, self).get_permissions()
