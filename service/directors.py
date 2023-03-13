from dao.directors import DirectorDAO
from dao.model.directors import DirectorSchema


director_schema = DirectorSchema()
directors_schema = DirectorSchema(many=True)
class DirectorService():
    def __init__(self, dao: DirectorDAO):
        self.dao = dao

    def get_all(self):
        return directors_schema.dump(self.dao.get_all_directors())

    def create(self, data):
        return director_schema.dump(self.dao.create(data))

    def get_one(self, id):
        return director_schema.dump(self.dao.get_one(id))

    def update(self, data):
        dir = self.dao.get_one(data['id'])
        if 'name' in data.keys():
            dir.name = data['name']
        self.dao.update(dir)
        return ''

    def delete(self, id):
        self.dao.delete(id)
        return ''