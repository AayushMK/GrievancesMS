from django.db import connection
import traceback
from model.user import User


class UserRepo(object):

    def saveUser(self, user, password):
        query = "INSERT INTO user(user_id, email, user_name, semester, password) VALUES(%s,%s,%s,%s,%s)"
        try:
            with connection.cursor() as cursor:
                cursor.execute(query, [user.user_id, user.email, user.user_name, user.semester, password])
                return True
        except Exception:
            traceback.print_exc()
            return False

    def signin(self, email):
        query = "SELECT user_id, email, user_name, semester, password FROM user WHERE email = %s"
        try:
            with connection.cursor() as cursor:
                cursor.execute(query, [email])
                row = cursor.fetchone()
                if row is None:
                    return None
                else:
                    user = User()
                    user.user_id = row[0]
                    user.email = row[1]
                    user.user_name = row[2]
                    user.semester = row[3]
                    return {"user": user, "password": row[4]}
        except Exception:
            traceback.print_exc()
            return False
