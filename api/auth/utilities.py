import re
from flask import jsonify, abort, make_response, Response


class validateUser:
    def __init__(self):
        pass


    @staticmethod
    def validate_names(name):
        """method validates user's names """
        return isinstance(name, str) and not re.search(r'[\s]', name)


    def validate_phoneNumber(self, number):
        """method validates user's phone number """
        return isinstance(number, int) and len(str(number)) < 14 and\
            len(str(number)) >= 9


    def validate_password(self, password):
        """method validates user's password """
        return isinstance(password, str) and len(password) >= 8 and\
            re.search(r'[0-9]', password)


    def verify_password(self, password1, password2):
        """
        method checks that the first password matches the second
        password
        """
        return password1 == password2 


    def check_missing_field(self, firstname, lastname,
                            email, phonenumber,password,
                            confirmpasswd):
        """
        Methods checks if a field is missing from the required fields
        """
        if not firstname:
            abort(make_response(jsonify({'error': 'firstname is missing',
                                         'status': 400}), 400))
        if not lastname:
            abort(make_response(jsonify({'error': 'lastname is missing',
                                         'status': 400}), 400))
        if not email:
            abort(make_response(jsonify({'error': 'email is missing',
                                         'status': 400}), 400))
        if not phonenumber:
            abort(make_response(jsonify({'error': 'phonenumber is missing',
                                         'status': 400}), 400))
        if not password:
            abort(make_response(jsonify({'error': 'password is required',
                                         'status': 400}), 400))
        if not confirmpasswd:
            abort(make_response(
                jsonify({'error': 'You must confirm your password to proceed',
                         'status': 400}), 400))


    def check_names(self, firstname, lastname):
        """
        Checks is the firstname and lastname are valid
        """
        if not validateUser.validate_names(firstname):
            abort(make_response(
                jsonify({'error': 'firstname cannot contain spaces and must be a string',
                         'status': 400}), 400))
        if not validateUser.validate_names(lastname):
            abort(make_response(
                jsonify({'error': 'laststname cannot contain spaces and must be a string',
                         'status': 400}), 400))
