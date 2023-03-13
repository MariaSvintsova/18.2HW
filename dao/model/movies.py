# здесь модель SQLAlchemy для сущности, также могут быть дополнительные методы работы с моделью (но не с базой, с базой мы работает в классе DAO)
from dao.model.genres import Genre
# Пример

from setup_db import db
from marshmallow import Schema, fields
from setup_db import db
from sqlalchemy.orm import relationship



class Movie(db.Model):
    __tablename__ = 'films'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    year = db.Column(db.Integer(), nullable=False)
    description = db.Column(db.String(100), nullable=False)
    trailer = db.Column(db.String(100), nullable=False)
    rating = db.Column(db.String(), nullable=False)
    genre_id = db.Column(db.Integer(), db.ForeignKey("genres.id"), nullable=False)
    genres_id = relationship("Genre")
    director_id = db.Column(db.Integer(), db.ForeignKey('directors.id'), nullable=False)
    directors_id = relationship('Director')


class MovieSchema(Schema):
    id = fields.Int()
    title = fields.Str()
    year = fields.Int()
    description = fields.Str()
    trailer = fields.Str()
    rating = fields.Str()
    genre_id = fields.Int()
    director_id = fields.Int()

