import pytest
from faker import Faker

from amazon_price_tracker.core.fixtures import user
from django.contrib.auth import SESSION_KEY, get_user_model
from django.test import client
from django.urls import reverse

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
    assert response.data["first_name"] == data["first_name"]

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
    assert response.data["first_name"] == user.first_name


def test_login_api_view_and_logout_api_view_200(client, db):
    """
    We need to create User Instance
    And then try to login with correct credentials
    """
    password = "Givemejob123!"
    email = faker.email()
    User.objects.create_user(email=email, password=password)

    url = reverse("account:login")
    data = {
        "email": email,
        "password": password,
    }
    response = client.post(url, data)
    assert response.status_code == 200
    assert SESSION_KEY in client.session

    url = reverse("account:logout")
    response = client.post(url)
    assert response.status_code == 200
    assert not SESSION_KEY in client.session


def test_login_api_view_400(client, db):
    """
    Try to login with random credentials
    """
    url = reverse("account:login")
    data = {
        "email": faker.email(),
        "password": faker.password(),
    }
    response = client.post(url, data)
    assert response.status_code == 400
    assert SESSION_KEY not in client.session
