from api.auth import views
from tests.base import BaseTest
import json


class UserTests(BaseTest):
    def test_returns_error_if_firstname_is_missing(self):
        data = {
                "names":"",
                "email":"ken@you.com",
                "phonenumber": "706578719",
                "password": "dfghjklkjhg3434",
                "confirmpassword":"dfghjklkjhg3434"

            }
        res = self.app.post('/api/v1/users', content_type="application/json",
        data=json.dumps(data))
        response_data = json.loads(res.data.decode())
        self.assertEqual(res.status_code,400)
        self.assertEqual(response_data['message'], "You must provide your names to proceed")


    def test_returns_error_if_lastname_is_missing(self):
        data = {
                "names": "ken",
                "email":"ken@you.com",
                "phonenumber": "706578719",
                "password": "dfghjklkjhg3434",
                "confirmpassword":"dfghjklkjhg3434"
                
            }
        res = self.app.post('/api/v1/users', content_type="application/json",
        data=json.dumps(data))
        response_data = json.loads(res.data.decode())
        self.assertEqual(res.status_code,400)
        self.assertEqual(response_data['message'], "Please provide your lastname")


    def test_returns_error_if_email_is_missing(self):
        data = {
                "names": "ken sanya",
                "phonenumber": "706578719",
                "password": "dfghjklkjhg3434",
                "confirmpassword":"dfghjklkjhg3434"
                
            }
        res = self.app.post('/api/v1/users', content_type="application/json",
        data=json.dumps(data))
        response_data = json.loads(res.data.decode())
        self.assertEqual(res.status_code,400)
        self.assertEqual(response_data['message'], "email is missing")     


    def test_returns_error_if_phonenumber_is_missing(self):
        data = {
                "names": "ken sanya",
                "email":"ken@you.com",
                "password": "dfghjklkjhg3434",
                "confirmpassword":"dfghjklkjhg3434"
                
            }
        res = self.app.post('/api/v1/users', content_type="application/json",
        data=json.dumps(data))
        response_data = json.loads(res.data.decode())
        self.assertEqual(res.status_code,400)
        self.assertEqual(response_data['message'], "phonenumber is missing") 


    def test_returns_error_if_password_is_missing(self):
        data = {
                "names": "ken sanya",
                "phonenumber": "706578719",
                "email":"ken@you.com",
                "confirmpassword":"dfghjklkjhg3434"
                
            }
        res = self.app.post('/api/v1/users', content_type="application/json",
        data=json.dumps(data))
        response_data = json.loads(res.data.decode())
        self.assertEqual(res.status_code,400)
        self.assertEqual(response_data['message'], "password is required")  


    def test_returns_error_if_passwords_dont_match(self):
        data = {
                "names": "ken sanya",
                "phonenumber": "706578719",
                "email":"ken@you.com",
                "password":"dfghjklkjhg3434",
                "confirmpassword":"dfghjklkjhg3434dfghjkjgfdfgh12332"
                
            }
        res = self.app.post('/api/v1/users', content_type="application/json",
        data=json.dumps(data))
        response_data = json.loads(res.data.decode())
        self.assertEqual(res.status_code,400)
        self.assertEqual(response_data['message'], "Passwords don't match") 


    def test_user_can_signup(self):
        data = {
                "names": "ken sanya",
                "email":"ken@you.com",
                "phonenumber": "706578719",
                "password": "dfghjklkjhg3434",
                "confirmpassword":"dfghjklkjhg3434"
                }
        res = self.app.post('/api/v1/users', content_type="application/json",
        data=json.dumps(data))
        response_data = json.loads(res.data.decode())
        self.assertEqual(res.status_code,201)
        self.assertEqual(response_data['message'], "Your account was successfuly created")


    def test_user_can_login(self):
        data = {
                "names": "pen youan",
                "email":"pen@you.com",
                "phonenumber": "706578718",
                "password": "dfghjklkjhg343411111",
                "confirmpassword":"dfghjklkjhg343411111"
                
            }
        user_data_login = {
            "email": "pen@you.com",
            "password": "dfghjklkjhg343411111"
        }
        self.app.post('/api/v1/users', content_type="application/json",
        data=json.dumps(data))
        res = self.app.post('/api/v1/users/login', content_type="application/json",
                            data=json.dumps(user_data_login))
        response_data = json.loads(res.data.decode())
        self.assertEqual(res.status_code,200)
        self.assertEqual(response_data['message'], "You are now loggedin")


    def test_gets_data_for_one_user(self):
        res = self.app.get('/api/v1/user', content_type="application/json",
        headers=self.user_header())
        response_data = json.loads(res.data.decode())
        self.assertEqual(res.status_code,200)
        self.assertEqual(response_data['status'], 200)
        self.assertIn("ten@you.com", response_data['data']['email'])


    def test_gets_data_for_all_users(self):
        res = self.app.get('/api/v1/users', content_type="application/json",
        headers=self.admin_header())
        response_data = json.loads(res.data.decode())
        self.assertEqual(res.status_code,200)
        self.assertEqual(response_data['status'], 200)
        self.assertIsInstance(response_data['data'], list)
