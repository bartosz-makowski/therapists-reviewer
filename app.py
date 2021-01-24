import os
from flask import (Flask, flash, 
    render_template, redirect, 
    request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)

@app.route('/')
@app.route('/home')
def home():
    """
    Function to load the homepage
    """
    return render_template('pages/home.html')


@app.route('/user-authentication', methods=["GET", "POST"])
def user_authentication():
    """
    Allows the user to register at the website
    Checks if user already exists in the DB 
    redirects user to homepage
    """
    if request.method == "POST":
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username is already in our database")
            return redirect(url_for('user_authentication'))
        
        username = request.form.get("username").lower()
        password = generate_password_hash(request.form.get("password"))

        mongo.db.users.insert_one({
            'username': username,
            'password': password
        })
        session["user"] = request.form.get("username").lower()
        flash("Registration successful, you are now logged in")

        if mongo.db.users.find_one({'username': username}) is not None:
            user = mongo.db.users.find_one({'username': username})
            user_id = user['_id']
            session['user_id'] = str(user_id)
            return redirect(url_for("home", user_id=user_id))

    return render_template('pages/user-authentication.html', registered=True)


@app.route('/get_therapists')
def get_therapists():
    """
    function to load list of therapists from db
    """
    therapists = mongo.db.therapists.find()
    return render_template('pages/therapists.html', therapists=therapists)


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)


