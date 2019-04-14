from flask import jsonify, abort, make_response
from flask import request, current_app as app
from functools import wraps
from api.auth.models import User
import re
import datetime
import jwt


class validateUser:
    def __init__(self):
        pass


    @staticmethod
    def validate_names(name):
        """method validates user's names """
        return isinstance(name[0], str) and isinstance(name[1], str) and\
            not re.search(r'[\s]', name[0]) and not re.search(r'[\s]', 
                                                              name[1])


    def validate_phoneNumber(self, number):
        """method validates user's phone number """
        return len(number) < 14 and\
            len(number) >= 9


    def remove_zero_from_number(self, number):
        temp_string = str(number)
        if temp_string[0] == '0':
            new = temp_string[1:]
            try:
                int(new)
                return new
            except:
                abort(make_response(
                    jsonify({'message': 'Only numbers allowed for the phonenumber field',
                            'status': 400}), 400))


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


    def check_missing_field(self, names, email, 
                            phonenumber,password,
                            confirmpasswd):
        """
        Methods checks if a field is missing from the required fields
        """
        if not names:
            abort(make_response(jsonify({
                'message': 'You must provide your names to proceed',
                'status': 400}), 400))
        if not email:
            abort(make_response(jsonify({'message': 'email is missing',
                                         'status': 400}), 400))
        if not phonenumber:
            abort(make_response(jsonify({'message': 'phonenumber is missing',
                                         'status': 400}), 400))
        if not password:
            abort(make_response(jsonify({'message': 'password is required',
                                         'status': 400}), 400))
        if not confirmpasswd:
            abort(make_response(
                jsonify({'message': 'You must confirm your password to proceed',
                         'status': 400}), 400))


    def check_split_names(self, names):
        if len(names) < 2:
            abort(make_response(
                jsonify({'message': 'Please provide your lastname',
                         'status': 400}), 400))
        if len(names) > 2:
            abort(make_response(
                jsonify({
                    'message': 'Only firstname and lastname are required for this field',
                    'status': 400
                    }), 400))


    def check_user_is_loggedin(self, current_user):
        if not current_user:
            abort(make_response(jsonify({'message': 'You are not loggedin',
                            'status': 403}), 403))


    def is_admin_user(self, current_user):
        if current_user.account_type != 'admin':
            abort(make_response(jsonify({'message':
                            'You are not allowed to perform this action',
                            'status': 403
                            }), 403))


    def check_names(self, names):
        """
        Checks is the firstname and lastname are valid
        """
        if not validateUser.validate_names(names[0]):
            abort(make_response(
                jsonify({'message': 'firstname cannot contain spaces and must be a string',
                         'status': 400}), 400))
        if not validateUser.validate_names(names[1]):
            abort(make_response(
                jsonify({'message': 'laststname cannot contain spaces and must be a string',
                         'status': 400}), 400))


def encode_token(user_email):
    """
    Generates authentication jwt token
    :param user_email:

    """
    try:
        payload = {
            # JWT expiration time
            'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=24),
            # issued at
            'iat': datetime.datetime.utcnow(),
            # token user info
            'sub': user_email
        }
        return jwt.encode(payload, app.config['SECRET'],
                          algorithm='HS256')
    except Exception as e:
        return e


def protected_route(f):
    """
    Decorator to protect routes
    """
    @wraps(f)
    def inner_func(*args, **kwargs):
        token = None
        if 'Authorization' in request.headers:
            token = request.headers['Authorization']
        if not token:
            return jsonify({'status': 401,
                            'message': 'Token is missing'}), 401
        try:
            data = jwt.decode(
                token, app.config['SECRET'], algorithms=['HS256'])
            current_user = User.query.filter_by(email=data['sub']).first()
        except jwt.ExpiredSignatureError:
            return jsonify({'status': 401,
                            'message': 'Token signature expired. Please login'}), 401
        except jwt.InvalidTokenError:
            return jsonify({'status': 401,
                            'message': 'Invalid token. Please login again'}), 401
        return f(current_user, *args, **kwargs)
    return inner_func
