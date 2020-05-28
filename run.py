from flask import Flask
from flask_restful import Api

from app.hoteis.action import Hoteis

app = Flask(__name__)
api = Api(app)

api.add_resource(Hoteis, '/hoteis')

if __name__ == '__main__':
    app.run(debug=True)

# http://127.0.0.1:5000/hoteis