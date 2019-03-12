from validate_email import validate_email
from api.auth.models import User
from api.database.db import db
from api.auth.utilities import validateUser
from flask import request, jsonify
from werkzeug.security import generate_password_hash,\
                        check_password_hash


class UserController:
    def __init__(self):
        pass


    def signup_user(self):
        data = request.get_json()
        firstname = data.get('firstname')
        lastname = data.get('lastname')
        email = data.get('email')
        phone_number = data.get('phonenumber')
        password = data.get('password')
        confirm_password = data.get('confirmpassword')
        user_validate = validateUser()
        # Check missing fields
        user_validate.check_missing_field(firstname, lastname, email,
                                phone_number, password, confirm_password)
        # validate names
        user_validate.check_names(firstname, lastname)
        # validate email
        if not validate_email(email, verify=False):
            return jsonify({'error': 'Email is not valid',
                            'status': 400}), 400
        # validate phonenumber
        if not user_validate.validate_phoneNumber(phone_number):
            return jsonify({'error': 'Phone number is not valid',
                            'status': 400}), 400
        # valid password
        if not user_validate.validate_password(password):
            return jsonify({
                'error': 'Password should be atleast 8 characters and should atleast one number',
                'status': 400
            }), 400
        # check if passwords match
        if not user_validate.verify_password(password, confirm_password):
            return jsonify({'error': "Passwords don't match",
                            'status': 400}), 400
        # hash the password to protect it
        password = generate_password_hash(password)
        # create the user
        user_data = User(firstname=firstname, lastname=lastname,
                        email=email, phone_number=phone_number,
                        password=password, account_type="normal")
        try:
            db.session.add(user_data)
            db.session.commit()
        except:
            return jsonify({'error': 'User account already exists', 
                            'status': 400}), 400
        return jsonify({'message': 'Your account was successfuly created',
                        'status': 201}), 201


    def login_user(self):
        login_data = request.get_json()
        user_email = login_data.get('email')
        user_password = login_data.get('password')
        user_login_data = User.query.filter_by(email=user_email).first()
        if user_login_data:
            if user_login_data.email == user_email and \
                check_password_hash(user_login_data.password, user_password):
                return jsonify({'message': 'You are now loggedin',
                'status': 200, 'access_token': 'coming soon'}), 200
        return jsonify({'error': 'Wrong email or password',
                        'status': 400}), 400
        