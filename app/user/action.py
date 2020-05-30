from typing import List
from uuid import uuid4

from database.repository import commit, save
from app.user.model import User


def create(data: dict) -> User:
    return save(User(id=str(uuid4()), login=data['login'], senha=data['senha']))


def get_by_login(login: str) -> User:
    return User.query.get(login)
