from django.db import connection
from model.grievance import Grievance
from model.user import User
from utils import to_date
import traceback


class GrievanceRepo(object):

    def saveGrievance(self, grievance):
        query = "INSERT INTO grievances(g_id, title, body, created_date, approvals, user_id) VALUES(%s,%s,%s,%s,%s,%s)"
        try:
            with connection.cursor() as cursor:
                cursor.execute(query, [grievance.g_id, grievance.title, grievance.body,
                                       grievance.created_date, grievance.approvals, grievance.user.user_id])
                return True
        except Exception:
            traceback.print_exc()
            return False

    def fetchGrievances(self):
        query = "SELECT title, body, created_date, approvals, user_id FROM grievances ORDER BY created_date DESC"
        context = {}
        try:
            with connection.cursor() as cursor:
                cursor.execute(query)
                rows = cursor.fetchall()
                if rows is None:
                    return None
                else:
                    grievances = list()
                    for row in rows:
                        g = Grievance()
                        g.title = row[0]
                        g.body = row[1]
                        g.created_date = row[2]
                        g.created_at = to_date(row[2])
                        g.approvals = row[3]
                        g.user = User()
                        g.user.user_id = row[4]
                        grievances.append(g)
                    return grievances
        except Exception as e:
            traceback.print_exc()
            return None
