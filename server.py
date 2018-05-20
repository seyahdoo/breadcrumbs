import os

from jinja2 import StrictUndefined

from flask import Flask, render_template, redirect, request, flash, session

from bson.objectid import ObjectId

from db import *

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get("FLASK_SECRET_KEY", "abcdef")
app.jinja_env.undefined = StrictUndefined

from raven.contrib.flask import Sentry
sentry = Sentry(app)


@app.route('/')
def index():
    """Homepage."""

    # look for user, if not user
    try:
        session["current_user"]["user_id"]
    except Exception as e:
        # go to login
        return redirect("/login")


    # if technician
    # go to my_issues

    # if shef
    # go to department_issues

    # if excecutive
    # go to reports

    # if admin
    # go to admin control panel

    return redirect("/new-issue")


@app.route("/login", methods=["GET"])
def show_login():
    """Show login form."""

    return render_template("login.html")


@app.route("/login", methods=["POST"])
def login():
    """Log user in if credentials provided are correct."""

    login_email = request.form.get("login_email")
    login_password = request.form.get("login_password")

    current_user = users.find_one({"email": login_email, "password": login_password})

    if current_user is None:
        flash("The email or password you have entered did not match our records. Please try again.", "danger")
        return redirect("/login")

    print(current_user)

    # Use a nested dictionary for session["current_user"] to store more than just user_id
    session["current_user"] = {
        "first_name": current_user["first_name"],
        "user_id": str(current_user["_id"]),
        "role": current_user["role"]
    }


    flash("Welcome {}. You have successfully logged in.".format(current_user["first_name"]), "success")

    return redirect("/")


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

    current_user = users.find_one({"email": signup_email})

    if current_user is None:
        new_user = {"email": signup_email,
                    "password": signup_password,
                    "first_name": first_name,
                    "last_name": last_name,
                    "role": "Issue_Enterer"}
        new_user_id = users.insert_one(new_user).inserted_id

        # Add same info to session for new user as per /login route
        session["current_user"] = {
            "first_name": new_user["first_name"],
            "user_id": str(new_user_id)
        }

        flash("You have succesfully signed up for an account, and you are now logged in.", "success")
        return redirect("/")

    flash("An account already exists with this email address. Please login.", "danger")
    return redirect("/login")


@app.route("/issue/<issue_id>/",  methods=["GET"])
def show_spesific_issue(issue_id):
    """Show spesific issue"""

    # grab spesific issue data from db
    try:
        iss =issues.find_one({"_id":ObjectId(issue_id)})

        # TODO if user have access

        # add to session
        flash("found spesific issue.", "success")
        return render_template("issue_detail.html",issue=iss)
    except Exception as e:
        flash("Could not found spesific issue.", "danger")
        #return redirect("/")

    return render_template("issue_detail.html")
    #return redirect("/")


@app.route("/new-issue",  methods=["GET"])
def new_issue_form():
    """Show new issue Form"""

    session.data  = [{"name":"Elektronik Fakultesi"},{"name":"Egitim Fakultesi"},{"name":"Insaat Fakultesi"},{"name":"Ogrenci Dekanligi"},{"name":"Enstituler"},{"name":"dfdsfdf"}]

    print(session["current_user"]["user_id"])
    session.issues = get_issues(session["current_user"]["user_id"])

    return render_template("issue_form.html")




@app.route("/new-issue",  methods=["POST"])
def new_issue_post():
    """File a new issue"""

    #Create new issue

    add_issue(request.form.get("birim_id"),
            session["current_user"]["user_id"],
            request.form.get("IssueType"),
            request.form.get("mesaj"),
            request.form.get("konu"))

    #populate issue

    flash("You have successfully filed an issue.", "success")
    # TODO redirect to issue id
    return redirect("/")


@app.route("/my_issues",  methods=["GET"])
def my_issues():
    """Show my attended issue list"""



    return render_template("issue_list.html")


@app.route("/department_issues",  methods=["GET"])
def department_issues():
    """Show department issue list to be assigned to technician"""

    return render_template("issue_list.html")


# eleman_ata?issue_id=1203&user_id=2201
@app.route("/eleman_ata",  methods=["GET"])
def eleman_ata():
    """Show my attended issue list"""

    issue_id = request.args.get('issue_id')
    user_id = request.args.get('user_id')

    # do assigning



    flash("You have successfully assigned technician to work.", "success")
    return redirect("/department_issues")



@app.route("/error")
def error():
    raise Exception("Error!")


#SayfalariOlusturmakIcinYaptim----omer#
@app.route("/technician", methods=["GET"])
def show_technician():
    """Show signup form."""


    return render_template("technician.html")

@app.route("/chief", methods=["GET"])
def show_chief():
    """Show signup form."""
    try:
        issues = get_issues(session["current_user"]["user_id"])
    except Exception as e:
        return redirect("/")


    return render_template("chief.html",issues=issues)

@app.route("/manager", methods=["GET"])
def show_manager():
    """Show signup form."""

    return render_template("manager.html")


@app.route("/admin", methods=["GET"])
def show_admin():
    """Show signup form."""

    return render_template("admin.html")


if __name__ == "__main__":
    # Set debug=True here to invoke the DebugToolbarExtension
    app.debug = True

    # Use the DebugToolbar
    # DebugToolbarExtension(app)

    PORT = int(os.environ.get("PORT", 8080))
    DEBUG = "NO_DEBUG" not in os.environ

    # app.run()
    app.run(host="localhost", port=PORT, debug=DEBUG)
