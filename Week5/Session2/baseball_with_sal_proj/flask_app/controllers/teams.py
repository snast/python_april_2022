from flask_app import app
from flask import Flask, render_template, redirect, session, request
from flask_app.models.team import Team
from flask_app.models.user import User


@app.route('/games/new')
def addGame():
    data = {
        'id': session['user_id']
    }
    theUser = User.getOne(data)
    return render_template('addGame.html', user=theUser)

@app.route('/games/create', methods=['post'])
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
    return redirect('/dashboard')

#Route to show a single game 
@app.route('/games/<int:id>')
def show_game(id):
    data = {
        'id': session['user_id']
    }
    theUser = User.getOne(data) # allowing us to display the sessioned user
    game_data = {
        'id': id
    }
    game = Team.getOne(game_data)
    return render_template('viewGame.html', user=theUser, game=game)

#Route to show edit form
@app.route('/games/<int:id>/edit')
def show_edit_form(id):
    data = {
        'id': session['user_id']
    }
    theUser = User.getOne(data) # allowing us to display the sessioned user
    game_data = {
        'id': id
    }
    game = Team.getOne(game_data)
    return render_template('editGame.html', user=theUser, game=game)

#Route to process edit form
@app.route('/games/<int:id>/update', methods=['POST'])
def edit_game(id):
    Team.update(request.form)
    return redirect(f'/games/{id}')

#Route to process delete form
@app.route('/games/<int:id>/delete', methods=['POST'])
def delete_game(id):
    # team_data = {
    #     'id': id
    # }
    Team.delete(request.form)
    return redirect('/dashboard')
