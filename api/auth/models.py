from api.database.db import db


class User(db.Model):

    user_id = db.Column('user_id',db.Integer, primary_key=True)
    firstname = db.Column('first_name',db.String(80), nullable=False)
    lastname = db.Column('last_name',db.String(80), nullable=False)
    email = db.Column('user_email',db.String(120), unique=True, nullable=False)
    phone_number = db.Column('phone_number',db.Text, nullable=False)
    password = db.Column('user_password',db.Text, unique=True, nullable=False)
    account_type = db.Column('account_type',db.String(20), nullable=False)

    
    def __repr__(self):
        return '<User %r>' % self.email
