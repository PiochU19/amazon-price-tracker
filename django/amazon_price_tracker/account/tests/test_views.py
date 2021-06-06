from django.http import response
import pytest
from faker import Faker

from amazon_price_tracker.core.fixtures import user
from django.test import client
from django.urls import reverse
from django.contrib.auth import get_user_model

faker = Faker()
User = get_user_model()


def test_user_register_201_created_and_400_due_email(client, db):
    url = reverse("account:user-list")
    data = {
        "email": faker.email(),
        "first_name": faker.first_name(),
        "last_name": faker.last_name(),
        "password": "Givemejobplz123!",
        "password_confirmation": "Givemejobplz123!",
    }
    response = client.post(url, data)
    assert response.status_code == 201
    assert response.data["email"] == data["email"]
    assert response.data["first_name"] == data["first_name"]
    assert response.data["last_name"] == data["last_name"]
    assert not response.data["is_active"]
    assert not response.data["is_staff"]

    user = User.objects.all().first()

    assert user.email == data["email"]
    assert user.first_name == data["first_name"]
    assert user.last_name == data["last_name"]
    assert not user.is_active
    assert not user.is_staff

    response = client.post(url, data)
    assert response.status_code == 400
    assert response.data["email"][0] == "user with this email already exists."


def test_user_register_400(client, db):
    url = reverse("account:user-list")
    data = {
        "email": faker.email(),
        "first_name": faker.first_name(),
        "last_name": faker.last_name(),
        "password": "Givemejobplz1!",
        "password_confirmation": "Givemejobplz123!",
    }
    response = client.post(url, data)
    ## two different passwords
    assert response.status_code == 400
    assert response.data["password"][0] == "passwords don't match"

    data["password"], data["password_confirmation"] = "badpass", "badpass"
    response = client.post(url, data)
    ## invalid password
    assert response.status_code == 400
    assert response.data["password"][0] == "invalid password"


def test_get_user_data_403(client, db):
    url = reverse("account:user-list")
    response = client.get(url)
    assert response.status_code == 403


def test_get_user_data_200(client, user):
    url = reverse("account:user-list")
    client.force_login(user)
    response = client.get(url)
    assert response.status_code == 200
    assert response.data["email"] == user.email
    assert response.data["first_name"] == user.first_name
    assert response.data["last_name"] == user.last_name
