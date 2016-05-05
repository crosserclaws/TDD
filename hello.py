#!/usr/bin/env python3

import requests
from flask import Flask

app = Flask(__name__)

@app.route("/encoding")
def encoding():
    url = 'https://news.ycombinator.com'
    resp = requests.get(url)
    return resp.headers['Content-Encoding']

@app.route("/hello")
def hello():
    return "Hello World!"

@app.route("/")
def index():
    return "This is an index page."

if __name__ == "__main__":
    app.run()
