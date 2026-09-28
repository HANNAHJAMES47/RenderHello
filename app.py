from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello! Welcome to Render PaaS."

@app.route("/about")
def about():
    return "This application is deployed on Render."