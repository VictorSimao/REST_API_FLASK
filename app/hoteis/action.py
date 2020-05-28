from flask_restful import Resource

from app.hoteis.model import hoteis


class Hoteis(Resource):
    def get(self):
        return {'hoteis': hoteis}
