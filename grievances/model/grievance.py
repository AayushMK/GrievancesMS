
class Grievance(object):
    def __init__(self):
        self.__g_id = None
        self.__title = None
        self.__body = None
        self.__created_at = None
        self.__created_date = None
        self.__approvals = None
        self.__user = None

    @property
    def g_id(self):
        return self.__g_id

    @property
    def title(self):
        return self.__title

    @property
    def body(self):
        return self.__body

    @property
    def created_at(self):
        return self.__created_at

    @property
    def created_date(self):
        return self.__created_date

    @property
    def approvals(self):
        return self.__approvals

    @property
    def user(self):
        return self.__user

    @g_id.setter
    def g_id(self, g_id):
        self.__g_id = g_id

    @title.setter
    def title(self, title):
        self.__title = title

    @body.setter
    def body(self, body):
        self.__body = body

    @created_at.setter
    def created_at(self, created_at):
        self.__created_at = created_at

    @created_date.setter
    def created_date(self, created_date):
        self.__created_date = created_date

    @approvals.setter
    def approvals(self, approvals):
        self.__approvals = approvals

    @user.setter
    def user(self, user):
        self.__user = user
