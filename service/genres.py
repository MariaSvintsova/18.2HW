from dao.genres import GenreDAO
from dao.model.genres import GenresSchema

genre_schema = GenresSchema()
genres_schema = GenresSchema(many=True)

class GenreServise():

    def __init__(self, dao: GenreDAO):
        self.dao = dao

    def create(self, data):
        return genre_schema.dump(self.dao.create(data))

    def get_all(self):
        return genres_schema.dump(self.dao.get_all_genres())

    def get_one(self, id):
        return genre_schema.dump(self.dao.get_one(id))

    def update(self, data):
        gen = self.dao.get_one(data['id'])
        if 'name' in data.keys():
            gen.name = data['name']
        self.dao.update(gen)
        return '', 204

    def delete(self, id):
        self.dao.delete(id)
        return ''