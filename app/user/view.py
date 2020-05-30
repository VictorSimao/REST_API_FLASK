from flask import Blueprint, jsonify, request
from flask_jwt_extended import create_access_token
from werkzeug.security import safe_str_cmp

from app.user.action import create as create_user, get_by_login as get_user_by_login

app_user = Blueprint('app_user', __name__)
app_userlogin = Blueprint('app_userlogin', __name__)


@app_user.route('/cadastro', methods=['POST'])
def post() -> tuple:
    payload = request.get_json()
    user = create_user(payload)
    return jsonify(user.serialize), 201


@app_userlogin.route('/login', methods=['POST'])
def post() -> tuple:
    payload = request.get_json()
    token_de_acesso = create_access_token(identity=payload['login'])
    return jsonify(token_de_acesso=token_de_acesso), 200
