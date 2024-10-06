from flask import session
from flask_mysqldb import MySQL
from datetime import datetime

class User:
    def __init__(self, app, bcrypt):
        self.app = app
        self.bcrypt = bcrypt
        db = MySQL()

    def get_users(self):
        response = {
            "error_fg": False,
            "error_msg": "",
            "data":""
        }

        db = MySQL()
        cursor = db.connection.cursor()
        try:
            user_list = cursor.execute("SELECT id, username ,email ,name  FROM orbiskpicom.tmp_jr_user tju")
            user_list = list(cursor.fetchall())
            response["data"] = user_list
        except Exception as e:
            response['error_fg'] = True
            response['error_msg'] = str(e)
        db.connection.commit()

        return response
    
    def create(self, created_by, username, email, password, name):
        response = {
            "error_fg": False,
            "error_msg": "",
            "data":""
        }

        db = MySQL()
        cursor = db.connection.cursor()
        try:

            created_at = datetime.now().date().strftime("%Y-%m-%d")
            hashed_password = self.bcrypt.generate_password_hash(password).decode('utf-8')

            cursor.execute("INSERT INTO tmp_jr_user (created_at, created_by, username, email, password, name) VALUES(%s, %s, %s, %s, %s, %s )", (created_at, created_by, username, email, hashed_password, name))
        except Exception as e:
            response['error_fg'] = True
            response['error_msg'] = str(e)
        db.connection.commit()

        return response
    
    def delete(self, user_id):
        response = {
            "error_fg": False,
            "error_msg": "",
            "data":""
        }

        db = MySQL()
        cursor = db.connection.cursor()
        try:

            cursor.execute("DELETE FROM orbiskpicom.tmp_jr_user WHERE id = %s ;", (user_id,))
            db.connection.commit()
        except Exception as e:
            response['error_fg'] = True
            response['error_msg'] = str(e)
        db.connection.commit()

        return response
    
    def update_password(self, user_id, password):
        response = {
            "error_fg": False,
            "error_msg": "",
            "data":""
        }

        db = MySQL()
        cursor = db.connection.cursor()
        try:

            hashed_password = self.bcrypt.generate_password_hash(password).decode('utf-8')

            cursor.execute('''
                            UPDATE orbiskpicom.tmp_jr_user 
                            SET password = %s WHERE id = %s''',(hashed_password, user_id))
            db.connection.commit()
            
        except Exception as e:
            response['error_fg'] = True
            response['error_msg'] = str(e)
        db.connection.commit()

        return response