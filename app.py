# основной файл приложения. здесь конфигурируется фласк, сервисы, SQLAlchemy и все остальное что требуется для приложения.
# этот файл часто является точкой входа в приложение

# Пример

from flask import Flask
from flask_restx import Api

from config import Config
from setup_db import db
from views.directors import directors_ns
from views.genres import genres_ns
# from views.directors import directors_ns
# from views.genres import genres_ns
from views.movies import movies_ns


# функция создания основного объекта app
def create_app(config_object):
    app = Flask(__name__)
    app.config.from_object(config_object)
    register_extensions(app)
    return app


# функция подключения расширений (Flask-SQLAlchemy, Flask-RESTx, ...)
def register_extensions(app):
    db.init_app(app)
    api = Api(app)
    api.add_namespace(movies_ns)
    api.add_namespace(genres_ns)
    api.add_namespace(directors_ns)





app = create_app(Config())
app.debug = True
with app.app_context():
    db.create_all()
    db.session.commit()

if __name__ == '__main__':
    app.run(host="localhost", port=10001, debug=True)
