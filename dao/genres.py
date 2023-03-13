from flask_sqlalchemy.session import Session
from marshmallow import Schema, fields
from setup_db import db
from dao.model.genres import Genre

class GenreDAO:
    def __init__(self, session: Session):
        self.session = session

    def get_all_genres(self):
        genres = Genre.query.all()
        return genres

    def get_one(self, gid):
        genre = Genre.query.get(gid)
        return genre

    def update(self, data):
        db.session.add(data)
        db.session.commit()
        return ''

    def delete(self, gid):
        gen = Genre.query.get(gid)
        if not gen:
            return 404
        db.session.delete(gen)
        db.session.commit()
        return ''

    def create(self, data):
        gen = Genre(**data)
        self.session.add(gen)
        self.session.commit()
        return ''