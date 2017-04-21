
# A very simple Flask Hello World app for you to get started with...

from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('credits.html')

@app.route('/login')
def login():
    return render_template('login.html')
