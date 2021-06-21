import pytest

from amazon_price_tracker.core.fixtures import admin, user
from amazon_price_tracker.core.utils import slugify_pl
from amazon_price_tracker.products.models import Product, Tracker
from django.test import client
from django.urls import reverse


def test_products_list_api_view_should_return_200(client, user):
    url = reverse("products:list_of_products")
    data = {
        "product_name": "Klocki Lego",
    }

    client.force_login(user, backend=None)
    response = client.post(url, data)

    assert response.status_code == 200
    assert len(response.data) > 0


def test_products_list_api_view_400(client, user):

    client.force_login(user, backend=None)
    url = reverse("products:list_of_products")

    assert client.post(url).status_code == 400

    data = {
        "product_name": "",
    }

    assert client.post(url, data).status_code == 400

    data = {
        "product_name": "sdgfdsfgdfgdfgdfgddasdfas",
    }

    assert client.post(url, data).status_code == 400


def test_products_list_api_view_throttle_rate(client, user):

    client.force_login(user, backend=None)
    url = reverse("products:list_of_products")
    data = {
        "product_name": "Klocki Lego",
    }

    for i in range(10):
        client.post(url, data)

    response = client.post(url, data)

    assert response.status_code == 429


def test_products_list_api_view_403(client):

    url = reverse("products:list_of_products")
    data = {
        "product_name": "Klocki Lego",
    }

    response = client.post(url, data)

    assert response.status_code == 403


def test_tracker_view_set_403(client):

    url = reverse("products:tracker-list")
    response = client.get(url)

    assert response.status_code == 403


def test_tracker_view_set(client, admin, user):
    client.force_login(admin, backend=None)
    url = reverse("products:tracker-list")

    data = {
        "price": 200,
        "link": "https://google.com",
        "product_name": "google",
        "image": "https://google.com/image",
    }

    response = client.post(url, data)

    assert response.status_code == 201

    product = Product.objects.get(name=data["product_name"])
    product_slug = slugify_pl(data["product_name"])

    assert product.link == data["link"]
    assert product.image == data["image"]
    assert product.slug == product_slug
    assert product.name == data["product_name"]

    assert Tracker.objects.get(product=product, user=admin)

    ## login to different user to test if he can delete not his tracker
    client.force_login(user, backend=None)
    url = reverse("products:tracker-detail", kwargs={"product__slug": product_slug})

    response = client.delete(url)

    assert response.status_code == 404

    client.force_login(admin)

    response = client.delete(url, backend=None)

    assert response.status_code == 204
