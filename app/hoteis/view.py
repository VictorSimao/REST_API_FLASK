from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required

from app.hoteis.action import create as create_hotel, get_all as get_all_hotel, \
    get_by_id as get_hotel_by_id, put as put_hotel

app_hotel = Blueprint('app_hotel', __name__)


@app_hotel.route('/hotel', methods=['GET'])
def get() -> tuple:
    return jsonify([hotel.serialize() for hotel in get_all_hotel()]), 200


@app_hotel.route('/hotel', methods=['POST'])
@jwt_required
def post() -> tuple:
    payload = request.get_json()
    hotel = create_hotel(payload)
    return jsonify(hotel.serialize()), 201


@app_hotel.route('/hotel/<id>', methods=['GET'])
@jwt_required
def get_by_id(id: str) -> tuple:
    hotel = get_hotel_by_id(id)
    return jsonify(hotel.serialize()), 200


@app_hotel.route('/hotel/<id>', methods=['PUT'])
@jwt_required
def put(id: str) -> tuple:
    payload = request.get_json()
    hotel = put_hotel(id, payload)
    return jsonify(hotel.serialize()), 201
