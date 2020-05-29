from typing import List
from uuid import uuid4

from database.repository import commit, save
from app.hoteis.model import Hotel


def create(data: dict) -> Hotel:
    return save(Hotel(id=str(uuid4()), nome=data['nome'], estrelas=data['estrelas'], diaria=data['diaria'],
                      cidade=data['cidade']))


def get_all() -> List[Hotel]:
    return Hotel.query.all()


def get_by_id(id: str) -> Hotel:
    return Hotel.query.get(id)


def put(id: str, data: dict) -> Hotel:
    hotel = get_by_id(id)
    hotel.nome = data['nome']
    hotel.estrelas = data['estrelas']
    hotel.diaria = data['diaria']
    hotel.cidade = data['cidade']
    commit()

    return hotel
