from database import db


class Hotel(db.Model):
    __tablename__ = 'hoteis'

    id = db.Column(db.String(36), primary_key=True, nullable=False)
    nome = db.Column(db.String(128), nullable=False)
    estrelas = db.Column(db.Float(precision=1), nullable=True)
    diaria = db.Column(db.Float(precision=2), nullable=True)
    cidade = db.Column(db.String(40), nullable=False)

    def serialize(self) -> dict:
        return {
            'id': self.id,
            'nome': self.nome,
            'estrelas': self.estrelas,
            'diaria': self.diaria,
            'cidade': self.cidade
        }
