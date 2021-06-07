from rest_framework import mixins, permissions, status, views, viewsets
from rest_framework.response import Response

from amazon_price_tracker.account.serializers import UserSerializer
from django.contrib.auth import authenticate, get_user_model, login, logout
from django.shortcuts import redirect

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


class UserLoginAPIView(views.APIView):
    """
    POST method where user is authenticated
    """

    permission_classes = [permissions.AllowAny]

    def post(self, request):
        data = request.data
        user = authenticate(email=data["email"], password=data["password"])
        if user is not None:
            login(request, user=user)
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)


class UserLogoutAPIView(views.APIView):
    """
    POST method where user logout
    """

    def post(self, request):
        logout(request)
        return Response(status=status.HTTP_200_OK)
