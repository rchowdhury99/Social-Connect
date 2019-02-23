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
    return render_template("login.html")

if __name__ == "__main__":
    app.run(debug=True)
