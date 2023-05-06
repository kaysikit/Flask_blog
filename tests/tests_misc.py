import pytest


def test_main(client):
    response = client.get("/")

    assert response.status_code == 200


def test_incorrect_logout(client):
    response = client.get("/logout", follow_redirects=True)
    assert response.request.path == "/login"
