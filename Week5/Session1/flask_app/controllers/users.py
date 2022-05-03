from flask_app import app
from flask import Flask, render_template, redirect, session, request
from flask_app.models.user import User
from flask_app.models.team import Team

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/createUser/', methods=['post'])
def createUser():
    data = {
        'firstName': request.form['firstName'],
        'lastName': request.form['lastName'],
        'email': request.form['email']
    }
    id = User.save(data)  # id = so that we can use id to put the user in session
    session['user_id'] = id # this just puts the user in session so that we can use the id for creating the game user_id
    print("creating user on controller file: ", id)
    return redirect('/dashboard/')

@app.route('/dashboard/')
def dashboard():
    print("the user: ", session['user_id'])
    data = {
        'id': session['user_id']
    }
    theUser = User.getOne(data) # allowing us to display the sessioned user
    theGames = Team.getAll()
    return render_template('dashboard.html', user=theUser, games=theGames)