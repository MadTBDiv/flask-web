import os

from flask import Flask

from config import Config
from data.database import db
from transport.routes import transport

basedir = os.path.abspath(os.path.dirname(__file__))


def create_app():
    # instantiate app
    app = Flask(__name__)
    app.config.from_object(Config)
    # initialize database
    db.init_app(app)
    with app.app_context():
        db.create_all()
    # register routes using blueprints
    app.register_blueprint(transport)
    return app


if __name__ == '__main__':
    app = create_app()
    app.run()
