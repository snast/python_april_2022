from flask import Flask, render_template  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"

@app.route('/hello')
def hello_world_with_no_number():
    return render_template('hello_world.html', my_count=5)
@app.route('/hello/<int:num>')          # The "@" decorator associates this route with the function immediately following
def hello_world(num):
    return render_template('hello_world.html', my_count=num)
@app.route('/welcome')
def welcome_with_no_name():
    return render_template('welcome_user.html', user_name="user".capitalize())
@app.route('/welcome/<string:name>')
def welcome(name):
    return render_template('welcome_user.html', user_name=name.capitalize())

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.