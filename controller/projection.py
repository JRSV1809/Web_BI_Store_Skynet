from flask import session
from flask_mysqldb import MySQL
from datetime import datetime
import uuid
from config import Config

class Projection:
    def __init__(self, app, bcrypt):
        self.app = app
        self.bcrypt = bcrypt
        db = MySQL()

    def get_url_projection_file(self):
        response = {
            "error_fg": False,
            "error_msg": "",
            "data":""
        }
        s3 = self.app.config['session_boto'].client('s3', region_name=Config.REGION_NAME)

        try:
            uid = uuid.uuid4()
            file_name = str(uid) + '.csv'
            response['data_name'] =  file_name
            response['data'] = s3.generate_presigned_url('put_object',
                                            Params={
                                                'Bucket': Config.BUCKET_S3,
                                                'Key': file_name,
                                                'ContentType': 'application/octet-stream'
                                                } ,
                                            ExpiresIn=3600)
        except Exception as e:
            response['error_fg'] = True
            response['error_msg'] = str(e)
        print(response)
        # The response contains the presigned URL
        return response

    def get_projections(self):
        response = {
            "error_fg": False,
            "error_msg": "",
            "data":""
        }

        db = MySQL()
        cursor = db.connection.cursor()
        try:
            projection_list = cursor.execute("SElECT tjp.id, tjp.created_at , tjp.name, tju.name as 'user_name' FROM orbiskpicom.tmp_jr_proyection tjp INNER JOIN orbiskpicom.tmp_jr_user tju ON tjp.created_by = tju.id ")
            projection_list = list(cursor.fetchall())
            response["data"] = projection_list
        except Exception as e:
            response['error_fg'] = True
            response['error_msg'] = str(e)
        db.connection.commit()

        return response
    
    def save(self, user_id, name, file):
        response = {
            "error_fg": False,
            "error_msg": "",
            "data":""
        }

        db = MySQL()
        cursor = db.connection.cursor()
        try:

            created_at = datetime.now().date().strftime("%Y-%m-%d")

            cursor.execute("INSERT INTO orbiskpicom.tmp_jr_proyection (created_by, created_at, name, file) VALUES (%s, %s, %s, %s)", (user_id, created_at, name, file))
        except Exception as e:
            response['error_fg'] = True
            response['error_msg'] = str(e)
        db.connection.commit()

        return response
    