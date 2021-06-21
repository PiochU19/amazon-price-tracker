from rest_framework import mixins, response, status, views, viewsets

from amazon_price_tracker.core.permissions import IsObjectOwner
from amazon_price_tracker.products.models import Tracker
from amazon_price_tracker.products.scrapper import Scrapper
from amazon_price_tracker.products.serializers import TrackerSerializer


class ProductsListAPIView(views.APIView):
    """
    APIView returns list of products
    scrapped from Amazon Site by POST method
    """

    throttle_scope = "get_list_of_products"

    def post(self, request):
        try:
            # validating if user provided
            # product name and if it's not empty

            product_name = request.data["product_name"]
            if product_name != "":

                list_of_products = Scrapper(product_name).get_list_of_products()

                if list_of_products:

                    return response.Response(
                        list_of_products,
                        status=status.HTTP_200_OK,
                    )

        except KeyError:
            pass

        return response.Response(status=status.HTTP_400_BAD_REQUEST)


class TrackerViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet,
):
    """
    Tracker Model View Set
    """

    queryset = Tracker.objects.all()
    serializer_class = TrackerSerializer
    permission_classes = [IsObjectOwner]
    lookup_field = "product__slug"

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        return Tracker.objects.filter(user=self.request.user)

    def get_throttles(self):
        """
        custom scoped throttle
        for POST method
        """

        if self.request.method == "POST":
            self.throttle_scope = "create_tracker"

        return super().get_throttles()
