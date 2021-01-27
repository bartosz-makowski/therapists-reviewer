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


@app.route('/register', methods=["GET", "POST"])
def register():
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
            return redirect(url_for('register'))
        
        username = request.form.get("username").lower()
        password = generate_password_hash(request.form.get("password"))

        mongo.db.users.insert_one({
            'username': username,
            'password': password
        })
        session["user"] = request.form.get("username").lower()
        flash("Registration successful, you are now logged in")
        

    return render_template('pages/user-authentication.html', register=True)


@app.route('/login', methods=["GET", "POST"])
def login():
    """
    checks if username exists
    checks if password is correct
    redirects to user-authentication.html
    """
    if request.method == "POST":
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})
        
        if existing_user:
            # check if username in db
            if check_password_hash(
                existing_user["password"], request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                flash("Welcome back! {}".format(request.form.get("username")))
            else:
                # invalid password match
                flash("Incorrect username or password")
                return redirect(url_for('register'))
            
        else:
            # username doesn't exist
            flash("Incorrect username or password")
            return redirect(url_for('register'))

    return render_template('pages/user-authentication.html')


@app.route('/logout')
def logout():
    """
    Logs user out from the session
    Redirects to login page
    """
    flash("You have logged out")
    session.clear()
    return redirect(url_for('login'))


@app.route('/user_profile')
def user_profile():
    feedbacks = mongo.db.reviews.find({"user": session["user"]})
    return render_template('/pages/user-profile.html', feedbacks=feedbacks)


@app.route('/leave_feedback', methods=["GET", "POST"])
def leave_feedback():
    if request.method == "POST":
        would_recommend = "on" if request.form.get('would_recommend') else "off"
        review = {
            "user": session["user"],
            'title': request.form.get('title'),
            'review_description': request.form.get('review_description'),
            'would_recommend': would_recommend,
            'therapist_id': request.form.get('select-therapist')
        }
        mongo.db.reviews.insert_one(review)
        flash("Feedback saved successfully")
        return redirect(url_for('leave_feedback'))

    therapists = mongo.db.therapists.find()
    return render_template('pages/leave-feedback.html', therapists=therapists)

@app.route('/get_therapists')
def get_therapists():
    """
    function to load list of therapists from db
    """
    therapists = mongo.db.therapists.find()
    return render_template('pages/therapists.html', therapists=therapists)


@app.route('/recommendations')
def recommendations():
    return render_template('pages/recommendations.html')


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)


