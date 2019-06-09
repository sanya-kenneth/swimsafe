from api.database.db import db
from api.auth.models import User
from werkzeug.security import generate_password_hash
from flask import current_app as app


# Admin for now
def create_admin():
    user_info = User.query.filter_by(email='sanyakenneth@gmail.com').first()
    if not user_info:
        password = generate_password_hash('adminpassword123')
        add_admin = User(firstname='admin', lastname='admin',
                         email='sanyakenneth@gmail.com', phone_number=706778714,
                         password=password, account_type="admin")
        db.session.add(add_admin)
        db.session.commit()
