import pytest
from flask import session


# Happy cases
def test_registration(client, login, password):
    response = client.post(
        "/register", data={"login": login, "password": password}, follow_redirects=True
    )
    assert response.status_code == 200
    assert response.request.path == "/login"


def test_auth(client, login, password):
    response = client.post(
        "login", data={"login": login, "password": password}, follow_redirects=True
    )

    assert response.status_code == 200
    assert session["name"] == login
    assert response.request.path == "/"


def test_logout(client, login, password):
    response = client.post(
        "login", data={"login": login, "password": password}, follow_redirects=True
    )

    assert response.status_code == 200
    assert session["name"] == login
    assert response.request.path == "/"

    response = client.get("/logout", follow_redirects=True)

    assert response.request.path == "/"
    assert session["name"] == None


# Bad cases
def test_incorrect_registration(client, login, password):
    response = client.post(
        "/register",
        data={"login": login.replace("_", " "), "password": password},
        follow_redirects=True,
    )
    assert response.request.path == "/register"


def test_incorrect_auth(client, login, password):
    response = client.post("/login", data={"login": login.replace("_", " ")})
    assert response.request.path == "/login"
