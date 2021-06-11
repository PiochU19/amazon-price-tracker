import pytest


from django.urls import reverse
from django.test import client


def test_products_list_api_view_should_return_200(client):
    url = reverse("products:list_of_products")
    data = {
        "product_name": "Klocki Lego",
    }

    response = client.post(url, data)

    assert response.status_code == 200
    assert len(response.data) == 45


def test_products_list_api_view_400(client):

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


def test_products_list_api_view_throttle_rate(client):
    url = reverse("products:list_of_products")
    data = {
        "product_name": "Klocki Lego",
    }

    for i in range(6):
        client.post(url, data)

    response = client.post(url, data)

    assert response.status_code == 429
