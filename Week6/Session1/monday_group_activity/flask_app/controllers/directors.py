from flask_app import app
from flask import render_template, request, redirect
from flask_app.models.director import Director

@app.route('/')
@app.route('/directors')
def directors():
    directors_from_the_db = Director.getAll()
    return render_template('directors.html', directors=directors_from_the_db)

@app.route('/directors/create', methods=['POST'])
def create_user():
    director_data = {
        'name': request.form['director_name']
    }
    if Director.validate_director(request.form):
    #Director.save(request.form)
        Director.save(director_data)
    return redirect('/directors')

# @app.route('/directors/<int:id>')
# #Route to show a single directors info

# Route to show edit form for a single director
@app.route('/directors/<int:id>/edit')
def edit_form(id):
    director_data = {
        'id': id
    }
    director = Director.getOne(director_data)
    return render_template('edit_director.html', director=director)

# Route to submit edit form
@app.route('/directors/<int:id>/update', methods=['POST'])
def update(id):
    director_data = {
        'id' : id,
        'name' : request.form['director_name'],
    }
    Director.update(director_data)
    return redirect(f'/directors/{id}/edit')