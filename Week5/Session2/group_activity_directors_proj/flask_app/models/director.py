from sqlite3 import connect
from flask_app.config.mysqlconnection import connectToMySQL

class Director:
    db = 'mydb'
    def __init__(self, data):
        self.id = data['id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.name = data['name']

    @classmethod
    def getAll(cls):
        query = 'SELECT * FROM directors'
        results = connectToMySQL(cls.db).query_db(query)
        directors = []
        #result is each row in the query
        for result in results:
            # director = Director(result)
            director = cls(result)
            directors.append(director)
        return directors

    @classmethod
    def save(cls, data):
        # data= { 'name': 'Kyle The Director' }
        query = 'INSERT INTO directors(name) VALUES(%(name)s);'
        return connectToMySQL(cls.db).query_db(query, data)
