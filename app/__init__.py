from flask import Flask
from database import db, migrate

from app.hoteis.view import app_hotel

def create_app():
    app = Flask(__name__)
    app.config.from_object('settings')
    db.init_app(app)
    migrate.init_app(app, db)
    _register_blueprint(app)
    return app


def _register_blueprint(app):
    app.register_blueprint(app_hotel)
