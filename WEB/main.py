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

@app.route("/signup")
@app.route("/signup/")
def signUp():
    return render_template("signup.html")

@app.route("/add_data", methods=["POST"])
def signup_client():
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
        print(data)
        return "0"

@app.route("/login")
@app.route("/login/")
def login():
    # renders the login page
    return render_template("login.html")

@app.route("/check", methods=["POST"])
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
        password = Database().login_info("db.db", "CLIENTS", data["email"])
        # check ther user name and password based on that redirect or just return an error
        if data["password"] == password:
            user_name = Database().get_user_info("db.db", "CLIENTS", data["email"])
            return render_template("profile.html", fname=user_name[0], lname=user_name[1])
        else:
            return render_template("404.html")

@app.route("/profile")
def get_user_profile():
    return render_template("profile.html")

if __name__ == "__main__":
    app.run(debug=True)
