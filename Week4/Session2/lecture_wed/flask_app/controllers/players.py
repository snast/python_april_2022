from flask import render_template, request, redirect, session
from flask_app import app

@app.route('/')          # The "@" decorator associates this route with the function immediately following
def hello_world():
    return 'Hello World!'  # Return the string 'Hello World!' as a response

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/players/create', methods=["POST"])
def create_player():
    print(request.form)
    ## STORE THE DATA SOMEWHERE
    # We will store the data in MySQL
    # Flask Session
    session['user_name'] = request.form['user_name']
    session['user_email'] = request.form['user_email']
    #request.form['user_name'] #Is a dictionary with key/value pairs from the form
    # return render_template('user_info.html', user_name=request.form['user_name'], email=request.form['user_email'])
    return redirect('/players/info')

@app.route('/players/info')
def player_info():
    return render_template('user_info.html')

@app.route('/players/clear')
def clear_player():
    session.clear()
    return redirect('/players/info')
