# здесь контроллеры/хендлеры/представления для обработки запросов (flask ручки). сюда импортируются сервисы из пакета service

# Пример
from flask_restx import Resource, Namespace
from implemented import director_service
from flask import request
directors_ns = Namespace('directors')

@directors_ns.route('/')
class DirectorView(Resource):
    def get(self):
        directors = director_service.get_all()
        return directors, 200

    def post(self):
        data = request.json
        nd = director_service.create(data)
        return nd, 201

@directors_ns.route('/<did>')
class DirectorView(Resource):

    def get(self, did):
        dir = director_service.get_one(did)
        return dir, 201

    def put(self, did):
        data = request.json
        director_service.update(data)
        return '', 201

    def delete(self, did):
        director_service.delete(did)
        return '', 204