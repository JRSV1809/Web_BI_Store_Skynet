from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_bcrypt import Bcrypt
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['SECRET_KEY'] = 'C3B688CCB7A13BBCE8CF59BBA5831'

#init Bcrypt
bcrypt = Bcrypt(app)

#Middleware
@app.before_request
def before_request():    
    if request.path.startswith('/app/'):
        if not session.get('user_id'):
            return redirect(url_for('login'))
    request.path = request.path.lower()
    if request.endpoint is None:
        return redirect(url_for('home'))
        
@app.route('/')
def home():
    return render_template("base.html")

@app.route('/login')
def login():
    if request.method == 'GET':
        return render_template('login.html')
    
    if request.method == 'POST':
        return True