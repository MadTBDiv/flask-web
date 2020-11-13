from flask import request, json, Blueprint

from data.database import db
from models.plant import decode_plant


transport = Blueprint('transport', __name__)


@transport.route('/dawn')
def hello_world():
    return 'New Dawn, New Day!'


@transport.route('/person', methods=['POST'])
def print_person():
    print(request.data)
    return 'OK'


@transport.route('/plant', methods=['POST'])
def create_plant():
    print(request.data)
    plant = json.loads(request.data, object_hook=decode_plant)
    db.session.add(plant)
    db.session.commit()
    print(plant.greenhouse_id)
    print(plant.name)
    print(plant.color)

    return 'OK'
