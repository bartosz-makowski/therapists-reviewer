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


@app.route('/results', methods=["GET", "POST"])
def search():
    """
    Allows user to search for therapists using
    location, main_therapy or other therapies
    """
    try:
        query = request.form.get("query").lower()
        therapists = mongo.db.therapists.find({"$text": {"$search": query}})
        count_therapists = therapists.count()
        return render_template('pages/search.html', therapists=therapists,
                               count_therapists=count_therapists)
    except:
        flash("Upps something went wrong, please try again later")
        return redirect(url_for('home'))


@app.route('/register', methods=["GET", "POST"])
def register():
    """
    Allows the user to register at the website
    Checks if user already exists in the DB
    Redirects user to homepage
    """
    if request.method == "POST":
        try:
            username = request.form.get("username", None).lower()
            if username is None:
                flash("Username cannot be empty")
                return redirect(url_for('register'))
            else:
                existing_user = mongo.db.users.find_one(
                    {"username": username})

                if existing_user:
                    flash("Username is already in our database")
                    return redirect(url_for('register'))

                password = generate_password_hash(request.form.get(
                    "password", None))
                if password is None:
                    flash("Password cannot be empty")
                    return redirect(url_for('register'))
                else:
                    mongo.db.users.insert_one({
                        'username': username,
                        'password': password
                    })
                    session["user"] = request.form.get("username").lower()
                    flash("Registration successful, you are now logged in")
                    return redirect(url_for('myaccount'))
        except:
            flash("Upps something went wrong, please try again later")
            return redirect(url_for('register'))
    return render_template('pages/user-authentication.html', register=True)


@app.route('/login', methods=["GET", "POST"])
def login():
    """
    Checks if username exists
    Checks if password is correct
    Redirects to user-authentication.html
    """
    if request.method == "POST":
        try:
            username = request.form.get("username", None).lower()
            if username is None:
                flash("Username cannot be empty")
                return redirect(url_for('login'))
            else:
                existing_user = mongo.db.users.find_one(
                    {"username": username})
                if existing_user:
                    # check if username in db
                    if check_password_hash(
                            existing_user["password"],
                            request.form.get("password")):
                        session["user"] = request.form.get("username").lower()
                        flash("Welcome back! {}".format(
                            request.form.get("username")))
                        return redirect(url_for('myaccount'))
                    else:
                        # invalid password match
                        flash("Incorrect username or password")
                        return redirect(url_for('login'))
                else:
                    # username doesn't exist
                    flash("Incorrect username or password")
                    return redirect(url_for('login'))
        except:
            flash("Upps something went wrong, please try again later")
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
    flash("Log out successful")
    return redirect(url_for('login'))


@app.route('/myaccount')
def myaccount():
    """
    Redirects user to their profile
    Page where all reviews from this user can be seen
    """
    try:
        feedbacks = mongo.db.reviews.find({"user": session["user"]})
        return render_template('/pages/myaccount.html', feedbacks=feedbacks)
    except:
        flash("Upps something went wrong, please try again later")
        return redirect(url_for('login'))


@app.route('/therapists')
def get_therapists():
    """
    Loads a list of therapists with their details from the db
    """
    try:
        therapists = mongo.db.therapists.find()
        return render_template('pages/therapists.html', therapists=therapists)
    except:
        flash("Upps something went wrong, please try again later")
        return redirect(url_for('get_therapists'))


@app.route('/therapist/profile/<therapist_id>/<feedback_id>')
def therapist_profile(therapist_id, feedback_id):
    """
    Shows a therapist's porfile page with their reviews
    """
    try:
        therapist = mongo.db.therapists.find_one(
            {"_id": ObjectId(therapist_id)})
        feedback = mongo.db.reviews.find({"therapist_id": feedback_id})
        return render_template('pages/therapist-profile.html',
                               therapist=therapist,
                               feedback=feedback)
    except:
        flash("Upps something went wrong, please try again later")
        return redirect(url_for('get_therapists'))


@app.route('/write-review', methods=["GET", "POST"])
def write_review():
    """
    Allows a user to leave a review for a therapist
    Redirects to review page
    """
    if request.method == "POST":
        try:
            review = {
                "user": session["user"],
                'title': request.form.get('title'),
                'email': request.form.get('email'),
                'review_description': request.form.get('review_description'),
                'therapist_id': request.form.get('select-therapist')
            }
            mongo.db.reviews.insert_one(review)
            flash("Review saved successfully")
            return redirect(url_for('write_review'))

        except:
            flash("Upps something went wrong, please try again later")
            return redirect(url_for('home'))

    therapists = mongo.db.therapists.find()
    return render_template('pages/review.html', therapists=therapists)


@app.route('/update-review/<feedback_id>', methods=["GET", "POST"])
def update_review(feedback_id):
    """
    Allows user to update changes to their review
    """
    if request.method == "POST":
        try:
            new_review = {
                "user": session["user"],
                'title': request.form.get('title'),
                'email': request.form.get('email'),
                'review_description': request.form.get('review_description'),
                'therapist_id': request.form.get('select-therapist')
            }
            mongo.db.reviews.update({"_id": ObjectId(feedback_id)}, new_review)
            flash("Review successfully updated")
            return redirect(url_for('myaccount'))
        except:
            flash("Upps something went wrong, please try again later")
            return redirect(url_for('myaccount'))

    therapists = mongo.db.therapists.find()
    feedback = mongo.db.reviews.find_one({"_id": ObjectId(feedback_id)})
    return render_template(
        '/pages/review.html',
        feedback=feedback,
        therapists=therapists,
        update=True
    )


@app.route('/delete-review/<feedback_id>')
def delete_review(feedback_id):
    """
    Allows a user to remove their review
    Redirects user to their profile page where all their reviews can be seen
    """
    try:
        mongo.db.reviews.remove({"_id": ObjectId(feedback_id)})
        flash("Review successfully deleted")
        return redirect(url_for('myaccount'))
    except:
        flash("Upps something went wrong, please try again later")
        return redirect(url_for('myaccount'))


@app.errorhandler(404)
def page_not_found(error):
    """
    Renders error.html with 404 message
    """
    error_message = str(error)
    return render_template('pages/error.html',
                           error_message=error_message), 404


@app.errorhandler(405)
def method_not_allowed(error):
    """
    Renders error.html with 405 message
    """
    error_message = str(error)
    return render_template('pages/error.html',
                           error_message=error_message), 405


@app.errorhandler(500)
def server_error(error):
    """
    Renders error.html with 500 message
    """
    error_message = str(error)
    return render_template('pages/error.html',
                           error_message=error_message), 500


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=False)
