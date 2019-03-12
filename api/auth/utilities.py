import re


class validateUser:
    def __init__(self):
        pass


    def validate_names(self, name):
        """method validates user's names """
        return isinstance(name, str) and not re.search(r'[\s]', name)


    def validate_phoneNumber(self, number):
        """method validates user's phone number """
        return isinstance(number, int) and len(str(number)) < 14


    def validate_password(self, password):
        """method validates user's password """
        return isinstance(password, str) and len(password) >= 8 and\
            re.search(r'[0-9]', password)
