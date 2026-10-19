class UserSite:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password

    @property
    def username(self):
        return self.__username

    @property
    def email(self):
        return self.__email

    @property
    def password(self):
        return self.__password

    @username.setter
    def username(self, new_username):
        self.__username = new_username

    @email.setter
    def email(self, new_email):
        self.__email = new_email

    @password.setter
    def password(self, new_password):
        self.__password = new_password