from flask_restx import Resource, Namespace
# здесь контроллеры/хендлеры/представления для обработки запросов (flask ручки). сюда импортируются сервисы из пакета service

# Пример
from flask_restx import Resource, Namespace
from implemented import movie_service
from flask import request
movies_ns = Namespace('movies')

@movies_ns.route('/')
class MoviesView(Resource):
    def get(self):
        try:
            director_id = request.args.get('director_id')
            genre_id = request.args.get('genre_id')
            year = request.args.get('year')
            if not director_id and not genre_id and not year:
                all_movies = movie_service.get_all()
                return all_movies, 200
            elif director_id:
                mov_by_dir = movie_service.get_by_director_id(director_id)
                return mov_by_dir, 200
            elif year:
                mov_by_year = movie_service.get_bu_year(year)
                return mov_by_year, 200
            else:
                mov_by_gen = movie_service.get_bu_genre_id(genre_id)
                return mov_by_gen, 200
        except Exception:
            raise

    def post(self):
        data = request.json
        movie = movie_service.create(data)
        return movie, 201


@movies_ns.route('/<int:movie_id>')
class MovieView(Resource):

    def get(self, movie_id):
        movie = movie_service.get_one(movie_id)
        return movie, 201

    def put(self, movie_id):
        data = request.json
        movie_service.update(data)
        return '', 201

    def delete(self, movie_id):
        movie_service.delete(movie_id)
        return '', 204

