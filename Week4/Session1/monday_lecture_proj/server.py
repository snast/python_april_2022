from flask import Flask, render_template  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"

sal = {
        'id': 1,
        'first_name': 'Sal',
        'last_name': 'Nast',
        'email': 'snast@codingdojo.com',
        'stacks': ['Python', 'Projects & Algorithms']
}
bob = {
        'id': 2,
        'first_name': 'Bob',
        'last_name': 'The Builder',
        'email': 'bbuilder@codingdojo.com',
        'stacks': ['MERN']
}
alice = {
        'id': 3,
        'first_name': 'Alice',
        'last_name': 'Avery',
        'email': 'aavery@codingdojo.com',
        'stacks': ['Java']
}

instructors = [sal, bob, alice]

@app.route('/')          # The "@" decorator associates this route with the function immediately following
def hello_world():
    return 'Hello World!'  # Return the string 'Hello World!' as a response
@app.route('/dashboard')
def dashboard():
    user_data = {
        'first_name': 'Sal',
        'last_name': 'Nast',
        'email': 'snast@codingdojo.com',
        'stacks': ['Python', 'Projects & Algorithms']
    }
    my_posts = ['My First Post', 'Another One', 'Final post']
    return render_template("dashboard.html", username=user_data, post = my_posts[2], instructors=instructors)

@app.route('/users/<int:id>')
def user(id):
    return render_template("user.html", user = instructors[id-1])
if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.