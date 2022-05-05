from flask_app import app
from flask import render_template, request, redirect
from flask_app.models.director import Director

@app.route('/directors')
def directors():
    directors_from_the_db = Director.getAll()
    return render_template('directors.html', directors=directors_from_the_db)

@app.route('/directors/create', methods=['POST'])
def create_user():
    director_data = {
        'name': request.form['director_name']
    }
    #Director.save(request.form)
    Director.save(director_data)
    return redirect('/directors')