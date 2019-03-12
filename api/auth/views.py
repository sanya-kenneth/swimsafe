from flask import jsonify
from api.auth import auth_bp
# from api.auth.models import User
from api.auth.controllers import UserController
from api.database.db import db


user = UserController()


@auth_bp.route('/users', methods=['POST'])
def register_user():
    return user.signup_user()


@auth_bp.route('/users/login', methods=['POST'])
def signin_user():
    return user.login_user()
