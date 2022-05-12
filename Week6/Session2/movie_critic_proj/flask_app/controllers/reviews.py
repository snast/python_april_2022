from flask import render_template, redirect, session, request, flash
from flask_app import app
from flask_app.models.user import User
from flask_app.models.review import Review
from datetime import datetime

from flask_bcrypt import Bcrypt        
bcrypt = Bcrypt(app) 

curr_date = datetime.now().strftime('%Y-%m-%d')
@app.route('/reviews')
def review_dashboard():
    user_data = {
        'id': session['user_id']
    }
    a_user = User.get_user_by_id(user_data)
    reviews = Review.getAll()
    return render_template('dashboard.html', user=a_user, reviews=reviews)

# Route to show create form, GET
@app.route('/reviews/new')
def create_form():
    return render_template('add_review.html', curr_date=curr_date) 

# Action tied to create form submittal, POST
@app.route('/reviews/create', methods=['POST'])
def create_review():
    #Send user back to create review form to fix missing/bad data
    if not Review.validate_review(request.form):
        return redirect('/reviews/new')

    # Check to see if the review form has bad info, if not, go ahead and create review!
    Review.create_review(request.form)
    return redirect('/reviews')
    

@app.route('/reviews/<int:id>')
def review(id):
    review_data = {
        'id': id
    }
    review = Review.getOne(review_data)
    return render_template('review.html', review=review)
#Route to show edit form, GET
@app.route('/reviews/<int:id>/edit')
def edit_form(id):
    review_data = {
        'id': id
    }
    review = Review.getOne(review_data)
    return render_template('edit_review.html', review=review)

@app.route('/reviews/<int:id>/update', methods=['POST'])
def update_review(id):
    if not Review.validate_review(request.form):
        return redirect(f'/reviews/{id}/edit')
    Review.update(request.form)
    return redirect(f'/reviews/{id}')

@app.route('/reviews/<int:id>/delete', methods=['POST'])
def delete_review(id):
    Review.delete(request.form)
    return redirect('/reviews')
