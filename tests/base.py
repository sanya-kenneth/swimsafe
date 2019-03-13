from api import create_app
from api.database.db import db
from api.auth.models import User
from flask import current_app as app
from werkzeug.security import generate_password_hash,\
    check_password_hash
import unittest
import json


class BaseTest(unittest.TestCase):
    def setUp(self):
        """
        This method helps setup tests.
        It also initialises the test_client where tests will be run 
        """
        self.app = create_app('Testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.app = self.app.test_client()
        self.create_admin()


    def tearDown(self):
        """
        This method will be called at the end of each individual test.
        It will help clear populated data by a particular test to prepare
        for the next test
        """
        db.session.remove()
        db.drop_all(app=app)


    def create_admin(self):
        user_info = User.query.filter_by(email='admin@gmail.com').first()
        if not user_info:
            password = generate_password_hash('adminpassword123')
            add_admin = User(firstname='admin', lastname='admin',
                        email='admin@gmail.com', phone_number=706778714,
                        password=password, account_type="admin")
            db.session.add(add_admin)
            db.session.commit()

    def get_user_token(self):
        user_data = {
                "firstname":"ten",
                "lastname":"10",
                "email":"ten@you.com",
                "phonenumber": 706578719,
                "password": "dlkjhgfdfghjjhgf88",
                "confirmpassword":"dlkjhgfdfghjjhgf88"
	
                    }
        user_data_login = {
            "email": "ten@you.com",
            "password": "dlkjhgfdfghjjhgf88"
        }
        self.app.post('/api/v1/users', content_type="application/json",
                      data=json.dumps(user_data))
        res = self.app.post('/api/v1/users/login', content_type="application/json",
                            data=json.dumps(user_data_login))
        data = json.loads(res.data.decode())
        return data


    def user_header(self):
        return {'content_type': "application/json", 'Authorization':
                self.get_user_token()['access_token']}


    def get_admin_token(self):
        admin_data_login = {
            "email": "admin@gmail.com",
            "password": "adminpassword123"
        }
        res = self.app.post('/api/v1/users/login', content_type="application/json",
                            data=json.dumps(admin_data_login))
        data = json.loads(res.data.decode())
        return data


    def admin_header(self):
        return {'content_type': "application/json", 'Authorization':
                self.get_admin_token()['access_token']}


if __name__=='__main__':
    unittest.main()
