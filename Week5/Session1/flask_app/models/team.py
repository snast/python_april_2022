from flask_app.config.mysqlconnection import connectToMySQL

class Team:
    db = 'sports'
    def __init__(self, data):
        self.id = data['id']
        self.team1 = data['team1']
        self.team2 = data['team2']
        self.finalScore = data['finalScore']
        self.gameInfo = data['gameInfo']
        self.gameDate = data['gameDate']
        self.createdAt = data['createdAt']
        self.updatedAt = data['updatedAt']
        self.user_id = data['user_id']

    def theTeams(self):
        return f'{self.team1} vs {self.team2}'

    @classmethod
    def getAll(cls):
        query = 'SELECT * from teams;'
        results = connectToMySQL(cls.db).query_db(query)
        teams = []
        for row in results:
            teams.append(cls(row))
        return teams

    @classmethod
    def getOne(cls, data):
        query = 'SELECT * from teams WHERE id = %(id)s;'
        results = connectToMySQL(cls.db).query_db(query, data)
        if len(results) < 1:
            return False
        return cls(results[0])

    @classmethod
    def save(cls, data):
        query = 'INSERT INTO teams (team1, team2, finalScore, gameInfo, gameDate, user_id) VALUES (%(team1)s, %(team2)s, %(finalScore)s, %(gameInfo)s, %(gameDate)s, %(user_id)s);'
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def update(cls, data):
        query = 'UPDATE teams SET team1=%(team1)s, team2=%(team2)s, finalScore=%(finalScore)s, gameInfo=%(gameInfo)s, gameDate=%(gameDate)s WHERE id = %(id)s;'
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def delete():
        query = 'DELETE FROM teams WHERE id = %(id)s;'
        return connectToMySQL(cls.db).query_db(query, data)