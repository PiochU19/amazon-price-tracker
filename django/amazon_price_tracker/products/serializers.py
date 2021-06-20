from rest_framework import serializers

from amazon_price_tracker.products.models import Product, Tracker


class ProductSerializer(serializers.ModelSerializer):
    """
    Serializer for Product Model
    For future "to_representation" method
    """

    class Meta:
        model = Product
        fields = ("slug", "name", "link", "image")


class TrackerSerializer(serializers.ModelSerializer):
    """
    Serializer for Tracker Model
    C
    """

    link = serializers.URLField(max_length=255, write_only=True)
    product_name = serializers.CharField(max_length=255, write_only=True)
    image = serializers.URLField(max_length=255, write_only=True)

    class Meta:
        model = Tracker
        fields = ("price", "link", "product_name", "image", "product")
        extra_kwargs = {
            "product": {
                "read_only": True,
            }
        }

    def create(self, data):
        """
        Override create method to customization
        """

        ## get obj if exist otherwise create
        product, product_created = Product.objects.get_or_create(
            name=data["product_name"],
            defaults={
                "link": data["link"],
                "image": data["image"],
            },
        )

        ## update obj with provided price if exist otherwise create
        tracker, tracker_created = Tracker.objects.update_or_create(
            product=product,
            user=data["user"],
            defaults={
                "price": data["price"],
            },
        )

        return tracker

    def to_representation(self, instance):
        """
        Product details will be displayed
        instead of pk
        """

        rep = super().to_representation(instance)
        rep["product"] = ProductSerializer(instance.product, many=False).data

        return rep
