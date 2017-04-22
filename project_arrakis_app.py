
# A very simple Flask Hello World app for you to get started with...

from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash

app = Flask(__name__)

app.config.update(dict(
    SECRET_KEY='test'
))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if( request.method=='POST'):
        if( request.form['username']!='fabio'):
            error='Invalid username'
        elif( request.form['password']!='fabio'):
            error='Invalid password'
        else:
            session['logged_in']=True
            session['username']=request.form['username']
            flash('Login successfull.')
            return redirect(url_for('index'))
    return render_template('login.html', error=error)

@app.route('/logout')
def logout():
    session.pop('logged_in')
    flash('Session ended')
    return redirect(url_for('index'))
