from api.auth import auth_bp
# from api.auth.models import User
from api.auth.controllers import UserController
from api.database.db import db
from api.auth.utilities import protected_route


user = UserController()


@auth_bp.route('/users', methods=['POST'])
def register_user():
    return user.signup_user()


@auth_bp.route('/users/login', methods=['POST'])
def signin_user():
    return user.login_user()


@auth_bp.route('/users', methods=['GET'])
@protected_route
def get_all_users(current_user):
    return user.fetch_users(current_user)


@auth_bp.route('/user', methods=['GET'])
@protected_route
def get_one_user(current_user):
    return user.fetch_user(current_user)


@auth_bp.route('/user', methods=['PUT'])
@protected_route
def update_user_info(current_user):
    return user.edit_user_info(current_user)
