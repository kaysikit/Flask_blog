from config import app
from flask_blog.views.view import view
from flask_session import Session


def create_app(app):
    app = app
    app.register_blueprint(view, url_prefix="")
    Session(app)
    return app


if __name__ == "__main__":
    create_app(app).run(debug=True)
