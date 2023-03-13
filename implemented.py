from dao.genres import GenreDAO
from dao.movies import MovieDAO
from dao.directors import DirectorDAO
from service.genres import GenreServise
from service.movies import MovieService
from service.directors import DirectorService
from setup_db import db

movies_dao = MovieDAO(db.session)
movie_service = MovieService(dao=movies_dao)

genres_dao = GenreDAO(db.session)
genre_service = GenreServise(dao=genres_dao)



directors_dao = DirectorDAO(db.session)
director_service = DirectorService(dao=directors_dao)

