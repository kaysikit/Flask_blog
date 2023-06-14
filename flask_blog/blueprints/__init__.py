from flask import Flask

from flask_blog.blueprints.autenfication import autenfication
from flask_blog.blueprints.misc import misc
from flask_blog.blueprints.user import user


def init_app(app: Flask):
    app.register_blueprint(misc)
    app.register_blueprint(user)
    app.register_blueprint(autenfication)
