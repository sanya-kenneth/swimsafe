from validate_email import validate_email
from api.auth.models import User
from api.database.db import db
from api.auth.utilities import validateUser, encode_token
from flask import request, jsonify
from werkzeug.security import generate_password_hash,\
                        check_password_hash


user_validate = validateUser()


class UserController:
    def __init__(self):
        pass


    def signup_user(self):
        data = request.get_json()
        # firstname = data.get('firstname')
        names = data.get('names')
        email = data.get('email')
        phone_number = data.get('phonenumber')
        password = data.get('password')
        confirm_password = data.get('confirmpassword')
        # Check missing fields
        user_validate.check_missing_field(names, email,
                                phone_number, password, confirm_password)
        # seperate firstname and lastname
        split_names = names.split()
        # check split names
        user_validate.check_split_names(split_names)
        first_name = split_names[0]
        last_name = split_names[1]
        # validate names
        user_validate.check_names(split_names)
        # validate email
        if not validate_email(email, verify=False):
            return jsonify({'message': 'Email is not valid',
                            'status': 400})
        # validate phonenumber
        if not user_validate.validate_phoneNumber(phone_number):
            return jsonify({'message': 'Phone number is not valid',
                            'status': 400})
        new_number = user_validate.remove_zero_from_number(phone_number)
        if new_number:
            phone_number = new_number
        else:
            phone_number = phone_number
        # valid password
        if not user_validate.validate_password(password):
            return jsonify({
                'message': 'Password should be atleast 8 characters and should atleast one number',
                'status': 400
            })
        # check if passwords match
        if not user_validate.verify_password(password, confirm_password):
            return jsonify({'message': "Passwords don't match",
                            'status': 400})
        # hash the password to protect it
        password = generate_password_hash(password)
        # check if user exists
        user_info = User.query.filter_by(email=email).first()
        if user_info:
            return jsonify({'message': 'User account already exists', 
                            'status': 400})
        # create the user
        user_data = User(firstname=first_name, lastname=last_name,
                        email=email, phone_number=phone_number,
                        password=password, account_type="normal")
        db.session.add(user_data)
        db.session.commit()
        return jsonify({'message': 'Your account was successfuly created',
                        'status': 201})


    def login_user(self):
        login_data = request.get_json()
        user_email = login_data.get('email')
        user_password = login_data.get('password')
        if not user_email or not user_password:
            return jsonify({'message': 'email and password fields are required',
                            'status': 400})
        user_login_data = User.query.filter_by(email=user_email).first()
        if user_login_data:
            if user_login_data.email == user_email and \
                check_password_hash(user_login_data.password, user_password):
                access_token = encode_token(user_email)
                return jsonify({'message': 'You are now loggedin',
                'status': 200, 'access_token': access_token.decode('UTF-8'),
                'account_type': user_login_data.account_type})
        return jsonify({'message': 'Wrong email or password',
                        'status': 400})
    

    def fetch_users(self, current_user):
        # Check if the user is loggedin
        user_validate.check_user_is_loggedin(current_user)
        # Check if the user is a admin
        user_validate.is_admin_user(current_user)
        display_list = []
        keys = ['userid', 'firstname', 'lastname', 'email', 'phonenumber',
                'account_type']
        user_list = User.query.all()
        for user_item in user_list:
            details = [user_item.user_id, user_item.firstname,
            user_item.lastname, user_item.email, user_item.phone_number,
            user_item.account_type]
            display_list.append(dict(zip(keys, details)))
        if not user_list:
            return jsonify({'message': 'There are no users registered yet',
                            'status': 404})
        return jsonify({'data':display_list, 
                        'status': 200})


    def fetch_user(self, current_user):
        # check if user is loggedin
        user_validate.check_user_is_loggedin(current_user)
        get_user = User.query.filter_by(user_id=current_user.user_id).first()
        if not get_user:
            return jsonify({'message': 'User record not found',
                            'status': 404})
        return_dict =  {
                        'user_id': get_user.user_id,
                        'firstname': get_user.firstname,
                        'lastname': get_user.lastname,
                        'email': get_user.email,
                        'phonenumber': get_user.phone_number,
                        'account_type': get_user.account_type
                      }
        return jsonify({'data': return_dict, 'status': 200})


    def update_user_data(self, query, column, new_data):
        setattr(query, column, new_data)
        db.session.commit()


    def set_default_if_none(self, user_query, firstname, lastname,
                            useremail, phonenumber):
        if not firstname:
            user_query.firstname = user_query.firstname
            db.session.commit()
        if not lastname:
            user_query.lastname = user_query.lastname
            db.session.commit()
        if not useremail:
            setattr(user_query, "email", user_query.email)
            db.session.commit()
        if not phonenumber:
            user_query.phone_number = user_query.phone_number
            db.session.commit()


    def edit_user_info(self, current_user):
        user_validate.check_user_is_loggedin(current_user)
        fetch_user = User.query.filter_by(user_id=current_user.user_id).first()
        data = request.get_json()
        f_name = data.get('first_name')
        l_name = data.get('last_name')
        user_email = data.get('email')
        user_phone_number = data.get('phone_number')
        # set data to original if none is provided
        self.set_default_if_none(fetch_user, f_name, l_name, user_email, user_phone_number)
        # Validate user firstame
        if f_name is not None:
            if not isinstance(f_name, str):
                return jsonify({'message': 'first name provided is not valid',
                                'status': 400})
            # update firstname if provided
            self.update_user_data(fetch_user, "firstname", f_name)
        # Validate user lastname
        if l_name is not None:
            if not isinstance(l_name, str):
                return jsonify({'message': 'last name provided is not valid',
                                'status': 400})
            # update lastname if provided
            self.update_user_data(fetch_user, "lastname", l_name)
        # validate email
        if user_email is not None:
            if not validate_email(user_email, verify=False):
                return jsonify({'message': 'Email is not valid',
                                'status': 400})
            # update user email if provided
            self.update_user_data(fetch_user, "email", user_email)
        # Validate user phonenumber
        if user_phone_number is not None:
            user_validate.validate_phoneNumber(user_phone_number)
            # update user phone number if provided
            self.update_user_data(fetch_user, "phone_number", user_phone_number)
        return jsonify({'message': 'We have updated your profile information',
                        'status': 202})
