from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app.models.user import User
import re

class Review:
    db = "movie_critic"

    def __init__(self, data):
        self.id = data['id']
        self.title = data['title']
        self.content = data['content']
        self.rating = data['rating']
        self.date_watched = data['date_watched']
        self.user_id = data['user_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user = None

    @classmethod
    def create_review(cls, data):
        query ="INSERT INTO reviews(title,content,rating,date_watched,user_id) VALUES(%(title)s,%(content)s, %(rating)s, %(date_watched)s, %(user_id)s);"
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def getAll(cls):
        query = 'SELECT * FROM reviews JOIN users ON reviews.user_id=users.id;'
        results = connectToMySQL(cls.db).query_db(query)
        reviews = []
        for row in results:
            #Create a review object
            review = cls(row)
            
            #Create a user object
            user_data = {
                'id': row['users.id'],
                'first_name': row['first_name'],
                'last_name': row['last_name'],
                'created_at': row['users.created_at'],
                'updated_at': row['users.updated_at'],
                'email': row['email'],
                'password': row['password']  
            }

            user = User(user_data)
            #associate user to the user's review
            review.user = user
            #Add review object to list of reviews
            reviews.append(review)

        return reviews
    @classmethod
    def getOne(cls, data):
        query = 'SELECT * FROM reviews JOIN users ON reviews.user_id=users.id WHERE reviews.id=%(id)s;'
        results = connectToMySQL(cls.db).query_db(query, data)
        if len(results) < 1:
            return False
        row = results[0]
        review = cls(row)
        user_data = {
                'id': row['users.id'],
                'first_name': row['first_name'],
                'last_name': row['last_name'],
                'created_at': row['users.created_at'],
                'updated_at': row['users.updated_at'],
                'email': row['email'],
                'password': row['password']  
            }

        user = User(user_data)
        #associate user to the user's review
        review.user = user
        return review
    @classmethod
    def update(cls, data):
        query='UPDATE reviews SET title=%(title)s,content=%(content)s,rating=%(rating)s,date_watched=%(date_watched)s WHERE id=%(id)s'
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def delete(cls, data):
        query='DELETE FROM reviews WHERE id=%(id)s'
        return connectToMySQL(cls.db).query_db(query, data)
    @staticmethod
    def validate_review(review):
        is_valid=True
        if len(review['title']) < 2:
            flash("Movie Title must be at least 3 characters", "error")
            is_valid = False
        if len(review['content']) < 2:
            flash("Review content must be at least 3 characters", "error")
            is_valid = False
        return is_valid
