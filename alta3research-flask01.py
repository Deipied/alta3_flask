#!/usr/bin/python3
# A Flask API that has two endpoints, with one being JSON output
from django.shortcuts import render
from flask import Flask
from flask import request
from flask import redirect
from flask import jsonify
from flask import render_template
from flask import url_for

# Flask constructor takes the name of current
# module (__name__) as argument
app = Flask(__name__)

# Random python dict to show usage
jason = [{'name': 'Spider-Man',
 'powers': ['wall crawling',
            'web shooters',
            'spider senses',
            'super human strength & agility'],
 'realName': 'Peter Parker',
 'since': 1962}]

# default path
@app.route("/")
def hello_world():
   return render_template("my.html")

@app.route("/success/<name>")
def success(name):
    return render_template("success.html", name = name)   

# second endpoint /json
@app.route("/spiderman")
def json_page():
    return jsonify(jason)

@app.route("/login", methods = ["POST", "GET"])
def login():
    # POST would likely come from a user interacting with postmaker.html
    if request.method == "POST":
        if request.form.get("nm"): # if nm was assigned via the POST
            user = request.form.get("nm") # grab the value of nm from the POST
        else: # if a user sent a post without nm then assign value defaultuser
            user = "defaultuser"
    # GET would likely come from a user interacting with a browser
    elif request.method == "GET":
        if request.args.get("nm"): # if nm was assigned as a parameter=value
            user = request.args.get("nm") # pull nm from localhost:5060/login?nm=larry
        else: # if nm was not passed...
            user = "defaultuser" # ...then user is just defaultuser
    return redirect(url_for("success", name = user)) # pass back to /success with val for name

if __name__ == "__main__":
   app.run(host="0.0.0.0", port=3000)