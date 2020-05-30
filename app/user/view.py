from flask import Blueprint, jsonify, request

from app.user.action import create as create_user, get_by_login as get_user_by_login

app_user = Blueprint('app_user', __name__)


@app_user.route('/user/<login>', methods=['GET'])
def get_by_login(login: str) -> tuple:
    user = get_user_by_login(login)
    return jsonify(user.serialize()), 200


@app_user.route('/cadastro', methods=['POST'])
def post() -> tuple:
    payload = request.get_json()
    user = create_user(payload)
    return jsonify(user.serialize()), 201


