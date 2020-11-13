from data.database import db


class Plant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    greenhouse_id = db.Column(db.Integer(), index=True)
    name = db.Column(db.String(128), index=True)
    color = db.Column(db.String(128), index=True)


def decode_plant(obj):
    return Plant(greenhouse_id=obj['greenhouse_id'], name=obj['name'], color=obj['color'])
