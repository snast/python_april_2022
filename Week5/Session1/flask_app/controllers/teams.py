from flask_app import app
from flask import Flask, render_template, redirect, session, request
from flask_app.models.team import Team
from flask_app.models.user import User


@app.route('/addGame/')
def addGame():
    data = {
        'id': session['user_id']
    }
    theUser = User.getOne(data)
    return render_template('addGame.html', user=theUser)

@app.route('/createGame/', methods=['post'])
def createGame():
    data = {
        'team1': request.form['team1'],
        'team2': request.form['team2'],
        'finalScore': request.form['finalScore'],
        'gameInfo': request.form['gameInfo'],
        'gameDate': request.form['gameDate'],
        'user_id': session['user_id']
    }
    Team.save(data) # no need to set a variable here as we are just saving to the database we don't need this in session
    print("creating game on controller: ", data)
    return redirect('/dashboard/')