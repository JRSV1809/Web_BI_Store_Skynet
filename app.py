from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_bcrypt import Bcrypt
from flask_mysqldb import MySQL
from config import Config
from controller.auth import Auth
from controller.user import User
from controller.projection import Projection
import boto3

app = Flask(__name__)

app.config['SECRET_KEY'] = 'C3B688CCB7A13BBCE8CF59BBA5831'

#mysql config
app.config["MYSQL_HOST"] = Config.DB_HOST
app.config["MYSQL_PORT"] = Config.DB_PORT
app.config["MYSQL_USER"] = Config.DB_USERNAME
app.config["MYSQL_PASSWORD"] = Config.DB_PASSWORD
app.config["MYSQL_DB"] = Config.DB_SCHEMA
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

app.config['session_boto'] = boto3.Session(
    aws_access_key_id = Config.AWS_ACCESS_KEY_ID,
    aws_secret_access_key = Config.AWS_SECRET_ACCESS_KEY
)

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
    
@app.route('/logout')
def logout():
    Auth(app, bcrypt).logout()
    return redirect(url_for('login'))

@app.route('/app/dashboard',methods=['GET', 'POST'])
def dashboard():
    if request.method == 'GET':
        data_welcome = Auth(app, bcrypt).welcome(session.get('user_id'))
        return render_template('dashboard.html', welcome = data_welcome)
    
    if request.method == 'POST':
        data = request.get_json()
        projection_create = Projection(app, bcrypt)

        if data['option'] == 'get_url_upload_file':
            return projection_create.get_url_projection_file()
        
        if data['option'] == 'save_projection':
            return projection_create.save(session.get('user_id'), data['name'], data['file'], data['date_from'], data['date_to'], data['days_to_project'])

@app.route('/app/user-managment',methods=['GET', 'POST'])
def user_managment():
    user_managment_controller = User(app, bcrypt)
    if request.method == 'GET':
        data_info = user_managment_controller.get_users()
        return render_template('user-managment.html', data_users = data_info['data'])
    
    if request.method == 'POST':
        data = request.get_json()

        if data['option'] == 'save_user':
            return user_managment_controller.create(session.get('user_id'), data['username'], data['email'], data['password'], data['name'] )
        
        if data['option'] == 'delete_user':
            return user_managment_controller.delete(data['id'])
        
        if data['option'] == 'reset_password':
            return user_managment_controller.update_password(data['id'], data['password'])
        
@app.route('/app/projections',methods=['GET', 'POST'])
def projections_managment():
    projection_controller = Projection(app,bcrypt)

    if request.method == 'GET':
        data_projection = projection_controller.get_projections()
        print(data_projection)
        return render_template('projection_managment.html', data_projection = data_projection['data'])
    
    if request.method == 'POST':
        data = request.get_json()
        projection_create = Projection(app, bcrypt)

        if data['option'] == 'get_url_upload_file':
            return projection_create.get_url_projection_file()
        
        if data['option'] == 'save_projection':
            return projection_create.save(session.get('user_id'), data['name'], data['file'], data['date_from'], data['date_to'], data['days_to_project'])