from flask import Flask

from flask_blog import config, blueprints


def create_app() -> Flask:
    app = Flask(__name__, static_folder='static')
    app.config.from_object(config)
    blueprints.init_app(app)

    return app
