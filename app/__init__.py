from flask import Flask
from database import db, migrate
from flask_jwt_extended import JWTManager

from app.hoteis.view import app_hotel
from app.user.view import app_user, app_userlogin

def create_app():
    app = Flask(__name__)
    app.config.from_object('settings')
    db.init_app(app)
    migrate.init_app(app, db)
    _register_blueprint(app)
    jwt = JWTManager(app)
    return app


def _register_blueprint(app):
    app.register_blueprint(app_hotel)
    app.register_blueprint(app_user)
    app.register_blueprint(app_userlogin)
