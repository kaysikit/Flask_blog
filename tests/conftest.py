from faker import Faker
import pytest
import responses

from flask_blog.app import create_app


@pytest.fixture(autouse=True)
def mock_response():
    with responses.RequestsMock() as requests_mock:
        yield requests_mock


@pytest.fixture(scope="session")
def app():
    app = create_app()
    app.config["WTF_CSRF_ENABLED"] = False
    return app


@pytest.fixture
def runner(app):
    return app.test_cli_runner()


@pytest.fixture(scope="session")
def login():
    return Faker().name().replace(" ", "_")


@pytest.fixture(scope="session")
def password():
    return Faker().password()
