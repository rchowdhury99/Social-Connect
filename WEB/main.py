import os
from datetime import datetime
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def main():
    return render_template("index.html")

@app.route("/login/")
def login():
    # renders the login page
    return render_template("login.html")

@app.route("/check", methods=["POST"])
# @app.route("/check/")
def check_login_creds():
    # checks login email and password to allow login
    if request.method == "POST":
        response = request.form
        print(response)
    return "hi"

if __name__ == "__main__":
    app.run(debug=True)
