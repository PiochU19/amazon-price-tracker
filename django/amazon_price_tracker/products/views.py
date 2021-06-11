from rest_framework import (
    views,
    response,
    status,
    permissions,
    viewsets,
    mixins,
)
from amazon_price_tracker.products.scrapper import Scrapper


class ProductsListAPIView(views.APIView):
    """
    APIView returns list of products
    scrapped from Amazon Site by POST method
    """

    permission_classes = [permissions.AllowAny]
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
