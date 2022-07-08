#!/usr/bin/python3
# A Flask API that has two endpoints, with one being JSON output
from flask import Flask
from flask import request
from flask import redirect
from flask import jsonify
from flask import render_template

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

# second endpoint /json
@app.route("/spiderman")
def json_page():
    return jsonify(jason)

if __name__ == "__main__":
   app.run(host="0.0.0.0", port=3000)