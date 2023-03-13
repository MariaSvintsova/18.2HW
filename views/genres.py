# здесь контроллеры/хендлеры/представления для обработки запросов (flask ручки). сюда импортируются сервисы из пакета service

# Пример
from flask_restx import Resource, Namespace
from implemented import genre_service
from flask import request
genres_ns = Namespace('genres')

@genres_ns.route('/')
class GenreView(Resource):
    def get(self):
        genres = genre_service.get_all()
        return genres, 200

    def post(self):
        data = request.json
        genre = genre_service.create(data)
        return genre, 201

@genres_ns.route('/<gid>')
class GenreView(Resource):

    def get(self, gid):
        gen = genre_service.get_one(gid)
        return gen, 201

    def put(self, gid):
        data = request.json
        genre_service.update(data)
        return '', 201

    def delete(self, gid):
        genre_service.delete(id)
        return '', 204