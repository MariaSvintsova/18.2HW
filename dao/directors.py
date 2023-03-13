from marshmallow import Schema, fields
from dao.model.directors import Director
from setup_db import db
class DirectorDAO:
    def __init__(self, session):
        self.session = session

    def get_all_directors(self):
        directors = Director.query.all()
        return directors

    def get_one(self, did):
        direct = Director.query.get(did)
        return direct

    def update(self, director):
        self.session.add(director)
        self.session.commit()
        return ''



    def delete(self, did):
        dir = Director.query.get(did)
        if not dir:
            return 404
        db.session.delete(dir)
        db.session.commit()
        return ''

    def create(self, data):
        dir = Director(**data)
        self.session.add(dir)
        self.session.commit()
        return ''