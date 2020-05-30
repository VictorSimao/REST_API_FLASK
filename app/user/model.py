from database import db


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.String(36), primary_key=True, nullable=False)
    login = db.Column(db.String(40), nullable=False)
    senha = db.Column(db.String(20), nullable=False)

    def serialize(self) -> dict:
        return {
            'id': self.id,
            'login': self.login
        }
