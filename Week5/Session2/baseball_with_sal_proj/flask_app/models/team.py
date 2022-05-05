from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.user import User

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
        self.user = None

    def theTeams(self):
        return f'{self.team1} vs {self.team2}'

    @classmethod
    def getAll(cls):
        query = 'SELECT * from teams JOIN users ON teams.user_id=users.id'
        results = connectToMySQL(cls.db).query_db(query)
        teams = []
        for row in results:
            team = cls(row)
            # after team = cls(row), team.user -> None
            user_data = {
                'id': row['users.id'],
                'firstName': row['firstName'],
                'lastName': row['lastName'],
                'email': row['email'], 
                'createdAt': row['users.createdAt'],
                'updatedAt': row['users.updatedAt'],
            }
            user = User(user_data)
            team.user = user           
            teams.append(team)
        return teams

    @classmethod
    def getOne(cls, data):
        query = 'SELECT * from teams JOIN users ON teams.user_id=users.id WHERE teams.id = %(id)s;'
        results = connectToMySQL(cls.db).query_db(query, data)
        if len(results) < 1:
            return False
        # assuming only one teams row per PK
        row = results[0]
        team = cls(row)
        # team.user -> None
        user_data = {
            'id': row['users.id'],
            'firstName': row['firstName'],
            'lastName': row['lastName'],
            'email': row['email'], 
            'createdAt': row['users.createdAt'],
            'updatedAt': row['users.updatedAt'],
        }
        user = User(user_data)
        team.user = user         
        return team

    @classmethod
    def save(cls, data):
        query = 'INSERT INTO teams (team1, team2, finalScore, gameInfo, gameDate, user_id) VALUES (%(team1)s, %(team2)s, %(finalScore)s, %(gameInfo)s, %(gameDate)s, %(user_id)s);'
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def update(cls, data):
        query = 'UPDATE teams SET team1=%(team1)s, team2=%(team2)s, finalScore=%(finalScore)s, gameInfo=%(gameInfo)s, gameDate=%(gameDate)s WHERE id = %(id)s;'
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def delete(cls, data):
        query = 'DELETE FROM teams WHERE id = %(id)s;'
        return connectToMySQL(cls.db).query_db(query, data)