from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_bcrypt import Bcrypt
from flask_mysqldb import MySQL
from config import Config
from controller.auth import Auth

app = Flask(__name__)

app.config['SECRET_KEY'] = 'C3B688CCB7A13BBCE8CF59BBA5831'

#mysql config
app.config["MYSQL_HOST"] = Config.DB_HOST
app.config["MYSQL_PORT"] = Config.DB_PORT
app.config["MYSQL_USER"] = Config.DB_USERNAME
app.config["MYSQL_PASSWORD"] = Config.DB_PASSWORD
app.config["MYSQL_DB"] = Config.DB_SCHEMA
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

#init Bcrypt
bcrypt = Bcrypt(app)

#init DB
db = MySQL(app)

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
    return redirect(url_for('login'))

@app.route('/login',methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        need_admin = Auth(app, bcrypt).need_admin()
        return render_template('login.html', need_admin = need_admin)
    
    if request.method == 'POST':
        data = request.get_json()

        if data['option'] == 'register_admin':
            return Auth(app, bcrypt).creat_user()
        
        if data['option'] == 'log_in':
            return Auth(app,bcrypt).login(data['username'], data['password'])
        return True