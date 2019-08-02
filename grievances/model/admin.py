class Admin(object):
    def __init__(self):
        self.__admin_id = None
        self.__admin_username = None
        self.__admin_password = None
        self.__admin_name = None

    @property
    def admin_id(self):
        return self.__admin_id

    @property
    def admin_username(self):
        return self.__admin_username

    @property
    def admin_password(self):
        return self.__admin_password

    @property
    def admin_name(self):
        return self.__admin_name

    @admin_id.setter
    def admin_id(self, admin_id):
        self.__admin_id = admin_id

    @admin_username.setter
    def email(self, admin_username):
        self.__admin_username = admin_username

    @admin_password.setter
    def user_name(self, admin_password):
        self.__admin_password = admin_password

    @admin_name.setter
    def semester(self, admin_name):
        self.__admin_name = admin_name
