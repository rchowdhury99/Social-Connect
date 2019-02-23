import os
from datetime import datetime
from flask import *
from helper import Database

app = Flask(__name__)

@app.route("/")
@app.route("/home")
# @app.route("/home/")
def main():
    return render_template("index.html")

@app.route("/login")
@app.route("/login/")
def login():
    # renders the login page
    return render_template("login.html")

@app.route("/check", methods=["POST"])
# @app.route("/check/", methods=["POST"])
# @app.route("/check/")
def check_login_creds():
    # checks login email and password to allow login
    if request.method == "POST":
        response = request.form
        data = {}
        cols = []
        vals = []
        # getting the email and password
        for i in response:
            vals.append(str(response[i]))
            cols.append(str(i))

        data = dict(zip(cols, vals))
        # check ther user name and password based on that redirect or just return an error

        return redirect(url_for("get_user_profile"))

@app.route("/profile")
def get_user_profile():
    x = "bob"
    return render_template("profile.html", fname=x )

if __name__ == "__main__":
    app.run(debug=True)
