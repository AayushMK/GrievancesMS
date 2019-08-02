class User(object):
    def __init__(self):
        self.__user_id = None
        self.__email = None
        self.__user_name = None
        self.__semester = None
        

    @property
    def user_id(self):
        return self.__user_id

    @property
    def email(self):
        return self.__email

    @property
    def user_name(self):
        return self.__user_name

    @property
    def semester(self):
        return self.__semester

    @user_id.setter
    def user_id(self, user_id):
        self.__user_id = user_id

    @email.setter
    def email(self, email):
        self.__email = email

    @user_name.setter
    def user_name(self, user_name):
        self.__user_name = user_name

    @semester.setter
    def semester(self, semester):
        self.__semester = semester
