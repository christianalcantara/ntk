import pytest
from rest_framework.test import APIClient
from rest_framework import status

from .mock import car_1, car_2, car_3, car_4, person

client = APIClient()


@pytest.mark.django_db
def test_add_car():
    response_person = client.post("/api/person/", person)
    data_person = response_person.data
    person_pk = data_person["id"]

    assert response_person.status_code == status.HTTP_201_CREATED

    car_1.update(person=person_pk)
    response = client.post("/api/car/", car_1)
    data = response.data

    assert data["name"] == car_1["name"]
    assert data["model"] == car_1["model"]
    assert data["color"] == car_1["color"]
    assert data["person"] == person_pk


@pytest.mark.django_db
def test_add_cars_to_not_sale_opportunity():
    response_person = client.post("/api/person/", person)
    data_person = response_person.data
    person_pk = data_person["id"]

    assert response_person.status_code == status.HTTP_201_CREATED

    # TODO: use parametrizer
    car_1.update(person=person_pk)
    client.post("/api/car/", car_1)

    car_2.update(person=person_pk)
    client.post("/api/car/", car_2)

    car_3.update(person=person_pk)
    client.post("/api/car/", car_3)

    car_4.update(person=person_pk)
    response = client.post("/api/car/", car_4)

    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert response.data["person"] == "Is not sale opportunity."
