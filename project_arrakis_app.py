# Login flask Application
import sqlalchemy
import models.models
import datetime

from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.models import Base, User

app = Flask(__name__)

app.config.update(dict(
    SECRET_KEY='test',
    SQLALCHEMY_ENGINE='mysql+mysqlconnector://ilbidi:fbidin88!!@ilbidi.mysql.pythonanywhere-services.com/ilbidi$projectarrakislogin'
))
app.config.from_envvar('PROJECT_ARRAKIS_SETTINGS', silent=True)

# Database management
db_engine = create_engine(app.config['SQLALCHEMY_ENGINE'], pool_timeout=20, pool_recycle=299)
Session = sessionmaker(bind=db_engine)
db_session = Session()
# Database destory and init
def project_arrakis_db_create():
    Base.metadata.create_all(db_engine)
def project_arrakis_db_destroy():
    Base.metadata.drop_all(db_engine)
def project_arrakis_db_init():
    u = User(username='fabio', fullname='Fabio Bidinotto', password='bidinotto', \
             dt_ins=datetime.datetime.now(), dt_upd=datetime.datetime.now())
    db_session.add(u)
    db_session.commit()

# Application

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if( request.method=='POST'):
        user = db_session.query(User).filter_by(username=request.form['username']).first()
        if( user == None ):
            error='Invalid username'
        elif( request.form['password']!=user.password):
            error='Invalid password'
        else:
            session['logged_in']=True
            session['username']=user.username
            session['fullname']=user.fullname
            session['password']=user.password
            flash('Login successfull.')
            return redirect(url_for('index'))
    return render_template('login.html', error=error)

@app.route('/logout')
def logout():
    session.pop('logged_in')
    flash('Session ended')
    return redirect(url_for('index'))
