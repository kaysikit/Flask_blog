import pytest


# Happe cases
def test_get_profile(client, login, password):
    response = client.post(
        "/register",
        data={
            "login": login + '2',
            "password": password,
        },
        follow_redirects=True,
    )
    assert response.request.path == "/login"
    response = client.post(
        "/login",
        data={
            "login": login + '2',
            "password": password,
        },
        follow_redirects=True,
    )
    assert response.request.path == "/"
    response = client.get("/profile")
    assert response.status_code == 200


# Bad cases
def test_incorrect_get_profile(client):
    response = client.get("/profile", follow_redirects=True)
    assert response.request.path == "/login"
