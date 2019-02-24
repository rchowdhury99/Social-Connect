# Social Connect - https://github.com/M-Faheem-Khan/Social-Connect/
# a tool to help you share mulitple social media accounts using one single web app

# RUN THIS FILE TO RUN THE APPLICATION

from flask import *
from helper import Database

# init
app = Flask(__name__)

# renders the home page
@app.route("/")
@app.route("/home")
def main():
    return render_template("index.html")

# renders the signup page
@app.route("/signup")
@app.route("/signup/")
def signUp():
    return render_template("signup.html")

# recieves the post request from the signup page
# add data to sqlite3 database
@app.route("/add_data", methods=["POST"])
def signup_client():
    if request.method == "POST":
        response = request.form
        cols = []
        vals = []
        # getting the email and password
        for i in response:
            vals.append(str(response[i]))
            cols.append(str(i))

        Database().add_client("db.db", "CLIENTS", cols, vals)
        return render_template("login.html")

# renders the login page
@app.route("/login")
@app.route("/login/")
def login():
    # renders the login page
    return render_template("login.html")

# validates the login credentional sent from the login screen as a POST request
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
            profile = Database().get_user_info("db.db", "CLIENTS", data["email"])
            return render_template("profile.html", email=data["email"], fname=profile[0], lname=profile[1], password=profile[2], fb_link=profile[3], insta_link=profile[4], twitter_link=profile[5], snapchat_link=profile[6])
        else:
            return render_template("404.html")

# render the profile
@app.route("/profile")
def get_user_profile():
    return render_template("profile.html")

# render the edit user profile information
@app.route("/edit-profile/<email>")
@app.route("/edit-profile/<email>/")
def get_user_data(email):
    profile = Database().get_user_info("db.db", "CLIENTS", email)
    return render_template("edit_profile.html", email=email, fname=profile[0], lname=profile[1], password=profile[2], fb_link=profile[3], insta_link=profile[4], twitter_link=profile[5], snapchat_link=profile[6])

# updates information in the database
@app.route("/update_info", methods=["POST"])
def update_user_info():
    if request.method == "POST":
        response = request.form
        cols = []
        vals = []
        # getting the email and password
        for i in response:
            vals.append(str(response[i]))
            cols.append(str(i))

        data = dict(zip(cols, vals))

        Database().update_user_profile("db.db", "CLIENTS", data["email"], cols, vals)
        profile = Database().get_user_info("db.db", "CLIENTS", data["email"])
        return render_template("edit_profile.html", email=data["email"], fname=profile[0], lname=profile[1], password=profile[2], fb_link=profile[3], insta_link=profile[4], twitter_link=profile[5], snapchat_link=profile[6])

# running the app
# add the host="0.0.0.0" to app.run() to run the program on local network
# it might not work due to tight security on the school network
if __name__ == "__main__":
    app.run(debug=False)
