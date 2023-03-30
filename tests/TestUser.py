import pytest
from app import create_app
from faker import Faker
from flask import session

faker = Faker()


@pytest.fixture
def app():
    app = create_app()
    app.config.update({
        "TESTING": True,
    })
    app.config['WTF_CSRF_ENABLED'] = False
    yield app


@pytest.fixture()
def client(app):
    return app.test_client()


@pytest.fixture()
def runner(app):
    return app.test_cli_runner()


# Happy cases

def test_request(client):
    response = client.get("/")
    assert b"<h1>You are logged in</h1>" or b"<h1>You are not logged in</h1>" in response.data


def test_auth(client):
    with client:
        response = client.post("/login", data={
            "login": "den_kaysik",
            "password": '95351575',
        }, follow_redirects=True)
        assert session["name"] == "den_kaysik"
        assert response.status_code == 200
        assert response.request.path == "/"


def test_logout_redirect(client):
    response = client.get("/logout")
    assert response.request.path == "/logout"


def test_register_user(client):
    response = client.post("/register", data={
        "login": faker.name().replace(' ', '_'),
        "password": faker.password(),
    }, follow_redirects=True)
    assert response.request.path == "/login"

# Bad Case

def test_auth_with_correct_login(client):
    response = client.post("/login", data={
        "login": "fFsfsgefg",
        "password": "ggregreg",
    }, follow_redirects=True)
    assert response.request.path == "/login"


def test_auth_with_incorrect_login(client):
    response = client.post("/login", data={
        "login": "fFsfs gefg",
        "password": "ggregreg",
    }, follow_redirects=True)
    assert response.request.path == "/login"


def test_register_with_incorrect_login(client):
    response = client.post("/register", data={
        "login": "Dawdwaf deferg",
        "password": "gdgre$3wr3",
    }, follow_redirects=True)
    assert response.request.path == "/register"


# Random value
def test_register_random_user_with_correct_login(client):
    response = client.post("/register", data={
        "login": faker.name().replace(' ', '_'),
        "password": faker.password(),
    }, follow_redirects=True)
    assert response.request.path == "/login"


def test_login_random_user_with_correct_login(client):
    response = client.post("/login", data={
        "login": faker.name().split()[0],
        "password": faker.password(),
    }, follow_redirects=True)
    assert response.request.path == "/login" or response.request.path == "/"

def test_register_random_user_with_incorrect_login(client):
    response = client.post("/register", data={
        "login": faker.name(),
        "password": faker.password(),
    }, follow_redirects=True)
    assert response.request.path == "/register"


def test_login_random_user_with_incorrect_login(client):
    response = client.post("/login", data={
        "login": faker.name(),
        "password": faker.password(),
    }, follow_redirects=True)
    assert response.request.path == "/login"


