import pytest
from rest_framework.test import APIClient
from rest_framework import status

client = APIClient()


@pytest.mark.django_db
def test_add_person():
    payload = {
        "name": "Christian",
        "email": "adm@gmail.com",
    }

    response = client.post("/api/person/", payload)
    data = response.data

    assert response.status_code == status.HTTP_201_CREATED
    assert data["name"] == payload["name"]
    assert data["email"] == payload["email"]
    assert data["sale_opportunity"]
