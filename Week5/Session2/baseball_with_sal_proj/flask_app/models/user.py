from flask_app.config.mysqlconnection import connectToMySQL

class User:
    db = 'sports'
    def __init__(self, data):
        self.id = data['id']
        self.firstName = data['firstName']
        self.lastName = data['lastName']
        self.email = data['email']
        self.createdAt = data['createdAt']
        self.updatedAt = data['updatedAt']
    
    def fullName(self):
        return f'{self.firstName} {self.lastName}'

    @classmethod
    def getAll(cls):
        query = 'SELECT * from users;'
        results = connectToMySQL(cls.db).query_db(query)
        users = []
        for row in results:
            users.append(cls(row))
        return users

    @classmethod
    def getOne(cls, data):
        query = 'SELECT * from users WHERE id = %(id)s;'
        results = connectToMySQL(cls.db).query_db(query, data)
        if len(results) < 1:
            return False
        return cls(results[0])

    @classmethod
    def save(cls, data):
        query = 'INSERT INTO users (firstName, lastName, email) VALUES (%(firstName)s, %(lastName)s, %(email)s);'
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def update():
        pass

    @classmethod
    def delete():
        pass
