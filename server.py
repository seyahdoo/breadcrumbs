"""Breadcrumbs: Tracking a user's restaurant history"""

import os

from jinja2 import StrictUndefined

from flask import Flask, render_template, redirect, request, flash, session, jsonify
from flask_debugtoolbar import DebugToolbarExtension

from model import User
from model import connect_to_db, db

from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy_searchable import search

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get("FLASK_SECRET_KEY", "abcdef")
app.jinja_env.undefined = StrictUndefined

from raven.contrib.flask import Sentry
sentry = Sentry(app)


@app.route('/')
def index():
    """Homepage."""

    return render_template("homepage.html")


@app.route("/login", methods=["GET"])
def show_login():
    """Show login form."""

    return render_template("login.html")


@app.route("/login", methods=["POST"])
def login():
    """Log user in if credentials provided are correct."""

    login_email = request.form.get("login_email")
    login_password = request.form.get("login_password")

    try:
        current_user = db.session.query(User).filter(User.email == login_email,
                                                     User.password == login_password).one()
    except NoResultFound:
        flash("The email or password you have entered did not match our records. Please try again.", "danger")
        return redirect("/login")

    # Use a nested dictionary for session["current_user"] to store more than just user_id
    session["current_user"] = {
        "first_name": current_user.first_name,
        "user_id": current_user.user_id
    }

    flash("Welcome {}. You have successfully logged in.".format(current_user.first_name), "success")

    return redirect("/users/{}".format(current_user.user_id))


@app.route("/logout")
def logout():
    """Log user out."""

    del session["current_user"]

    flash("Goodbye! You have successfully logged out.", "success")

    return redirect("/")


@app.route("/signup", methods=["GET"])
def show_signup():
    """Show signup form."""

    return render_template("signup.html")


@app.route("/signup", methods=["POST"])
def signup():
    """Check if user exists in database, otherwise add user to database."""

    signup_email = request.form.get("signup_email")
    signup_password = request.form.get("signup_password")
    first_name = request.form.get("first_name")
    last_name = request.form.get("last_name")

    try:
        db.session.query(User).filter(User.email == signup_email).one()

    except NoResultFound:
        new_user = User(city_id=city_id,
                        email=signup_email,
                        password=signup_password,
                        first_name=first_name,
                        last_name=last_name)
        db.session.add(new_user)
        db.session.commit()

        # Add same info to session for new user as per /login route
        session["current_user"] = {
            "first_name": new_user.first_name,
            "user_id": new_user.user_id
        }

        flash("You have succesfully signed up for an account, and you are now logged in.", "success")

        return redirect("/users/%s" % new_user.user_id)

    flash("An account already exists with this email address. Please login.", "danger")

    return redirect("/login")


@app.route("/error")
def error():
    raise Exception("Error!")


if __name__ == "__main__":
    # Set debug=True here to invoke the DebugToolbarExtension
    app.debug = True

    # connect_to_db(app)
    connect_to_db(app, os.environ.get("DATABASE_URL"))
    db.create_all()

    # Use the DebugToolbar
    # DebugToolbarExtension(app)

    PORT = int(os.environ.get("PORT", 8080))
    DEBUG = "NO_DEBUG" not in os.environ

    # app.run()
    app.run(host="0.0.0.0", port=PORT, debug=DEBUG)
