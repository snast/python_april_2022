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
        self.creator = None
        self.user_ids_who_favorited = []
        self.users_who_favorited = []

    @classmethod
    def create_review(cls, data):
        query ="INSERT INTO reviews(title,content,rating,date_watched,user_id) VALUES(%(title)s,%(content)s, %(rating)s, %(date_watched)s, %(user_id)s);"
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def getAll(cls):
        # query = 'SELECT * FROM reviews JOIN users ON reviews.user_id=users.id;'
        query='''SELECT * FROM reviews 
                JOIN users AS creators ON reviews.user_id=creators.id
                LEFT JOIN favorited_reviews ON favorited_reviews.review_id=reviews.id
                LEFT JOIN users AS users_who_favorited ON favorited_reviews.user_id = users_who_favorited.id;'''
        results = connectToMySQL(cls.db).query_db(query)
        reviews = []
        for row in results:
            new_review = True
            user_who_favorite_data = {
                'id': row['users_who_favorited.id'],
                'first_name': row['users_who_favorited.first_name'],
                'last_name': row['users_who_favorited.last_name'],
                'created_at': row['users_who_favorited.created_at'],
                'updated_at': row['users_who_favorited.updated_at'],
                'email': row['users_who_favorited.email'],
                'password': row['users_who_favorited.password']  
            }

            # Check to see if previously processed review, belongs to the same as current row
            number_of_reviews = len(reviews)

            # We have processed a row already
            if number_of_reviews > 0:
                # Check to see if the last review, is the same as the current row's
                last_review = reviews[number_of_reviews-1]
                if last_review.id == row['id']:
                    last_review.user_ids_who_favorited.append(row['users_who_favorited.id'])
                    last_review.users_who_favorited.append(User(user_who_favorite_data))
                    new_review = False

            # Create new review object is review has not been created and added to the list
            if new_review:
                #Create a review object
                review = cls(row)
                
                #Create a user object
                user_data = {
                    'id': row['creators.id'],
                    'first_name': row['first_name'],
                    'last_name': row['last_name'],
                    'created_at': row['creators.created_at'],
                    'updated_at': row['creators.updated_at'],
                    'email': row['email'],
                    'password': row['password']  
                }

                creator = User(user_data)
                #associate user to the user's review
                review.creator = creator
                
                #Check to see if any user liked this review, if someone did favorite, add to favs list
                if row['users_who_favorited.id']:
                    review.user_ids_who_favorited.append(row['users_who_favorited.id'])
                    review.users_who_favorited.append(User(user_who_favorite_data))

                #Add review object to list of reviews
                reviews.append(review)

        return reviews
        
    @classmethod
    def getOne(cls, data):
        # query = 'SELECT * FROM reviews JOIN users ON reviews.user_id=users.id WHERE reviews.id=%(id)s;'
        query='''SELECT * FROM reviews 
                JOIN users AS creators ON reviews.user_id=creators.id
                LEFT JOIN favorited_reviews ON favorited_reviews.review_id=reviews.id
                LEFT JOIN users AS users_who_favorited ON favorited_reviews.user_id = users_who_favorited.id
                WHERE reviews.id = %(id)s;'''
        
        results = connectToMySQL(cls.db).query_db(query, data)
        if len(results) < 1:
            return False

        new_review = True
        for row in results:
            #if this is the first row being processed
            if new_review:
                review = cls(row)
                #Create a user object
                user_data = {
                    'id': row['creators.id'],
                    'first_name': row['first_name'],
                    'last_name': row['last_name'],
                    'created_at': row['creators.created_at'],
                    'updated_at': row['creators.updated_at'],
                    'email': row['email'],
                    'password': row['password']  
                }
                creator = User(user_data)
                review.creator = creator
                new_review = False
            
            if row['users_who_favorited.id']:
                user_who_favorited_data = {
                    'id': row['users_who_favorited.id'],
                    'first_name': row['users_who_favorited.first_name'],
                    'last_name': row['users_who_favorited.last_name'],
                    'created_at': row['users_who_favorited.created_at'],
                    'updated_at': row['users_who_favorited.updated_at'],
                    'email': row['users_who_favorited.email'],
                    'password': row['users_who_favorited.password']  
                }
                user_who_favorited = User(user_who_favorited_data)
                review.users_who_favorited.append(user_who_favorited)
                review.user_ids_who_favorited.append(row['users_who_favorited.id'])
                
        return review

    @classmethod
    def update(cls, data):
        query='UPDATE reviews SET title=%(title)s, content=%(content)s,rating=%(rating)s,date_watched=%(date_watched)s WHERE id=%(id)s'
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def delete(cls, data):
        query='DELETE FROM reviews WHERE id=%(id)s'
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def favorite(cls, data):
        query='INSERT INTO favorited_reviews(user_id, review_id) VALUES(%(user_id)s, %(id)s);'
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def unfavorite(cls, data):
        query='DELETE FROM favorited_reviews WHERE user_id=%(user_id)s AND review_id=%(id)s;'
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

    @staticmethod
    def validate_edit(review):
        is_valid=True
        review_row = Review.getOne(review)
        if not review_row:
            flash(f"Review with id: {review['id']} does not exist", "error")
            is_valid = False
        else:
            if len(review['title']) < 2:
                flash("Movie Title must be at least 3 characters", "error")
                is_valid = False
            if len(review['content']) < 2:
                flash("Review content must be at least 3 characters", "error")
                is_valid = False
        return is_valid