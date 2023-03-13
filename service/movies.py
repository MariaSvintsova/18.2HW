from dao.movies import MovieDAO
from dao.model.movies import MovieSchema

movie_schema = MovieSchema()
movies_schema = MovieSchema(many=True)


class MovieService():
    def __init__(self, dao: MovieDAO):
        self.dao = dao
    def create(self, data):
        return movie_schema.dump(self.dao.create(data))

    def get_all(self):
        re = self.dao.get_all_movies()
        return movies_schema.dump(re)
        # return movies_schema.dump(self.dao.get_all_movies()[0])

    def get_one(self, id):
        return movie_schema.dump(self.dao.get_one(id))

    def update(self, data):
        mov = self.dao.get_one(data['id'])
        if 'name' in data.keys():
            mov.name = data['name']
        self.dao.update(mov)
        return ''

    def delete(self, id):
        self.dao.delete(id)
        return ''

    def get_by_director_id(self, director_id):
        mov = self.dao.get_by_director(director_id)
        return movies_schema.dump(mov[0])

    def get_bu_genre_id(self, genre_id):
        mov = self.dao.get_by_genre(genre_id)
        return movies_schema.dump(mov)

    def get_bu_year(self, year):
        mov = self.dao.get_bu_year(year)
        return movies_schema.dump(mov)