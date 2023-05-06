from flask import Flask

from flask_blog.blueprints.misc import misc
from flask_blog.blueprints.view import view


def init_app(app: Flask):
    app.register_blueprint(misc)
    app.register_blueprint(view)
