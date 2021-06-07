import os


from rest_framework import mixins, permissions, status, views, viewsets
from rest_framework.response import Response

from amazon_price_tracker.account.serializers import UserSerializer
from django.contrib.auth import authenticate, get_user_model, login, logout
from django.shortcuts import redirect
from django.views import View
from django.utils.encoding import force_text
from django.utils.http import urlsafe_base64_decode
from django.shortcuts import redirect
from amazon_price_tracker.account.tokens import token_generator_for_activate_account
from django.core.exceptions import ObjectDoesNotExist

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


class UserAccountActivateView(View):
    """
    View where user is activated
    """

    def get(self, request, upkb64, token):
        try:
            upk = force_text(urlsafe_base64_decode(upkb64))
            user = User.objects.get(pk=upk)
        except (TypeError, ValueError, OverflowError, ObjectDoesNotExist):
            pass

        if user is not None and token_generator_for_activate_account.check_token(
            user, token
        ):
            user.is_active = True
            user.save()

            return redirect(os.environ.get("PATH_SERVER"))

        return redirect(os.environ.get("PATH_SERVER") + "/404")
