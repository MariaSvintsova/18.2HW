from marshmallow import Schema, fields
from setup_db import db
class Director(db.Model):
    __tablename__ = 'directors'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)


class DirectorSchema(Schema):
    id = fields.Int()
    name = fields.Str()

