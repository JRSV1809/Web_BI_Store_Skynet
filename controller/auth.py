from flask import session
from flask_mysqldb import MySQL
from datetime import datetime

class Auth:
    def __init__(self, app, bcrypt):
        self.app = app
        self.bcrypt = bcrypt
        db = MySQL()

    def creat_user(self):

        response = {
            "error_fg": False,
            "error_msg": "",
            "data":""
        }

        db = MySQL()
        cursor = db.connection.cursor()

        created_at = datetime.now().date().strftime("%Y-%m-%d")
        username = "admin"
        email = "admin@mail.com"
        password = "123456"
        name = "Administrador Global"

        hashed_password = self.bcrypt.generate_password_hash(password).decode('utf-8')

        cursor.execute("INSERT INTO tmp_jr_user (created_at, created_by, username, email, password, name) VALUES(%s, %s, %s, %s, %s, %s )", (created_at, 0, username, email, hashed_password, name))
        db.connection.commit()

        response["data"] = {
            'user_info': {
                "username":username,
                "email":email,
                "password": password
            }
        }
        
        return response

    def need_admin(self):
        db = MySQL()
        cursor = db.connection.cursor()

        count_user = cursor.execute("SELECT COUNT(*) as 'found' FROM tmp_jr_user",)
        count_user = cursor.fetchone()
        
        if count_user['found'] == 0:
            return True
        else:
            return False

    def login(self, username, password):
        response = {
            "error_fg": False,
            "error_msg": "",
            "data":""
        }

        db = MySQL()
        cursor = db.connection.cursor()

        cursor.execute("SELECT email, password, id FROM tmp_jr_user WHERE email=%s or username=%s", (username, username,))
        user = cursor.fetchone()

        if user is not None:
            if self.bcrypt.check_password_hash(user['password'], password):
                #set session variables
                session['user_id'] = user['id']
                response["data"] = {'redirect_url':'/app/dashboard'}
            else:
                response["error_fg"] = True
                response["error_msg"] = "Unable to login with those credentials, please check your email/username or password and try again."
        else:   
            response["error_fg"] = True
            response["error_msg"] = "Unable to login with those credentials, please check your email/username or password and try again."
        return response

    def creat_new_user(self, is_first, username, email, pasword, name, user_id_created):

        response = {
            "error_fg": False,
            "error_msg": "",
            "data":""
        }

        db = MySQL()
        cursor = db.connection.cursor()