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
        return redirect(url_for('user_profile'))
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
                return redirect(url_for('user_profile'))
            else:
                # invalid password match
                flash("Incorrect username or password")
                return redirect(url_for('login'))
        else:
            # username doesn't exist
            flash("Incorrect username or password")
            return redirect(url_for('login'))

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
    """
    Redirects user to their profile
    page where all reviews from this user can be seen
    """
    feedbacks = mongo.db.reviews.find({"user": session["user"]})
    return render_template('/pages/user-profile.html', feedbacks=feedbacks)


@app.route('/leave_feedback', methods=["GET", "POST"])
def leave_feedback():
    """
    Allows a user to leave a review for a therapist
    Redirects to leave-feedback page
    """
    if request.method == "POST":
        review = {
            "user": session["user"],
            'title': request.form.get('title'),
            'email': request.form.get('email'),
            'review_description': request.form.get('review_description'),
            'therapist_id': request.form.get('select-therapist')
        }
        mongo.db.reviews.insert_one(review)
        flash("Feedback saved successfully")
        return redirect(url_for('leave_feedback'))

    therapists = mongo.db.therapists.find()
    return render_template('pages/leave-feedback.html', therapists=therapists)


@app.route('/update_review/<feedback_id>', methods=["GET", "POST"])
def update_review(feedback_id):
    """
    Allows user to update changes to their review
    """
    if request.method == "POST":
        new_review = {
            "user": session["user"],
            'title': request.form.get('title'),
            'email': request.form.get('email'),
            'review_description': request.form.get('review_description'),
            'therapist_id': request.form.get('select-therapist')
        }
        mongo.db.reviews.update({"_id": ObjectId(feedback_id)}, new_review)
        flash("Feedback successfully updated")
        return redirect(url_for('user_profile'))

    therapists = mongo.db.therapists.find()
    feedback = mongo.db.reviews.find_one({"_id": ObjectId(feedback_id)})
    return render_template(
        '/pages/update-review.html',
        feedback=feedback,
        therapists=therapists
    )


@app.route('/delete_review/<feedback_id>')
def delete_review(feedback_id):
    """
    Allows a user to remove their review
    Redirects user to their profile page where all their reviews can be seen
    """
    mongo.db.reviews.remove({"_id": ObjectId(feedback_id)})
    flash("Review successfully deleted")
    return redirect(url_for('user_profile'))


@app.route('/get_therapists')
def get_therapists():
    """
    Loads a list of therapists with their details from the db
    """
    therapists = mongo.db.therapists.find()
    return render_template('pages/therapists.html', therapists=therapists)


@app.route('/therapist_profile/<therapist_id>/<feedback_id>')
def therapist_profile(therapist_id, feedback_id):
    """
    Shows a therapist's porfile page with their reviews
    """
    therapist = mongo.db.therapists.find_one({"_id": ObjectId(therapist_id)})
    feedback = mongo.db.reviews.find({"therapist_id": feedback_id})
    return render_template('pages/therapist-profile.html',
                           therapist=therapist,
                           feedback=feedback
                           )


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=os.environ.get('debug'))
