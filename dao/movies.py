# это файл для классов доступа к данным (Data Access Object). Здесь должен быть класс с методами доступа к данным
# здесь в методах можно построить сложные запросы к БД

# Например
from marshmallow import Schema, fields
from sqlalchemy.orm.session import Session

from dao.model.directors import Director
from dao.model.genres import Genre
from dao.model.movies import Movie

class MovieDAO:
    def __init__(self, session: Session):
        self.session = session

    def get_all_movies(self):
        movies = self.session.query(Movie).all()
        return movies
        # movies = Movie.query.all()
        # return movies

    def get_one(self, mid):
        movie = Movie.query.get(mid)
        return movie

    def update(self, data):
        self.session.add(data)
        self.session.commit()
        return ''

    def delete(self, mid):
        mov = Movie.query.get(mid)
        if not mov:
            return 404
        self.session.delete(mov)
        self.session.commit()
        return '', 204

    def create(self, data):
        mov = Movie(**data)
        self.session.add(mov)
        self.session.commit()
        return '', 204

    def get_by_director(self, director_id):
        mov = Movie.query.join(Director, Director.id == Movie.director_id).filter(director_id == Director.id).all()
        return mov, 204

    def get_by_genre(self, genre_id):
        mov = Movie.query.join(Genre, genre_id == Movie.genre_id).all()
        return mov
        # return Movie.query.join(Genre, Genre.id == genre_id).all()

    def get_bu_year(self, yyyear):
        # mov = Movie.query.filter(yyyear == Movie.year).all()
        return Movie.query.filter(Movie.year == yyyear)
        # return Movie.query.filter(Movie.year == yyyear)