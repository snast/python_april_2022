from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

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
    def getOne(cls, data):
        query = 'SELECT * FROM directors WHERE id=%(id)s;'
        results = connectToMySQL(cls.db).query_db(query, data)
        # since we know, id is unique, we can assume there is only one result
        result = results[0]
        director = cls(result)
        return director

    @classmethod
    def save(cls, data):
        # data= { 'name': 'Kyle The Director' }
        query = 'INSERT INTO directors(name) VALUES(%(name)s);'
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def update(cls, data):
        query= 'UPDATE directors SET name=%(name)s WHERE id=%(id)s;'
        return connectToMySQL(cls.db).query_db(query, data)

    #validate_director is going to take in a dictionary representing the form input
    @staticmethod
    def validate_director(director):
        "director = { 'director_name': 'Bob The Builder' }"
        # director_name needs to have at least 3 characters
        is_valid = True

        if len(director['director_name']) < 3:
            is_valid = False
            flash('Director name needs to be at least 3 characters', 'error')

        return is_valid

