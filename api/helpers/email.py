from flask_mail import Mail, Message
from flask import request, jsonify, current_app as app
from api.pools.models import Pool
from api.trainers.models import Trainer
from api.auth.models import User
from api.auth.utilities import validateUser


validate_user = validateUser()


def send_trainer_info(current_user, trainer_id):
    data = request.get_json()
    user_email = data.get('user_email')
    if user_email:
        user = User.query.filter_by(email=user_email).first()
        if not user:
            return jsonify({'message': 'User was not found', 'status': 404}), 404
    mail = Mail(app)
    trainer = Trainer.query.get(trainer_id)
    if not trainer:
        return jsonify({'message': 'Trainer was not found',
                        'status': 404}), 404
    msg = Message('Trainer Information', sender='easyswim123@gmail.com',
                  recipients=[user_email])
    msg.html = f"""\
                <html>
                <head>
                </head>
                <body>
                        <p
                    style="
                        color: #063769; 
                        "
                    >
                        <a style="color: black;">Dear</a> {user.firstname} {user.lastname}.</b>.
                    </p>
                    <p>Thank you for making a training request</p>
                    <p
                        style="
                        color: #bbc4cc; 
                        background-color: #37474f;  
                        border-radius: 5px;
                        padding-left: 5px;
                        padding-top: 10px;
                        padding-bottom: 10px;
                        "
                    >
                        <a style="font-size: 19px; color: #eeeeee;"><b>Trainer information</b></a>
                        <br>
                        First name:         {trainer.first_name}
                        <br>
                        Last name:          {trainer.last_name}
                        <br>
                        Description:        {trainer.description}
                        <br>
                        Trainer contact:    {trainer.trainer_contact}
                        <br>
                        Working time:       {trainer.working_time}
                        <br>
                        Availabity:         {trainer.available}
                        <br>
                        
                    </p>
                     <img src='{trainer.trainer_img}' height='350px' width='500px'>
                </body>
                </html>
                """
    mail.send(msg)
    return jsonify({'message': 'Email was successfuly sent to user', 'status': 200})


def send_email(current_user, pool_id):
    mail = Mail(app)
    data = request.get_json()
    pool_request = data.get("pool_request")
    user_fname = current_user.firstname
    user_lname = current_user.lastname
    user_phone_number = current_user.phone_number
    user_email = current_user.email
    if str(pool_request) == 'training':
        pool = Pool.query.get(pool_id)
        if not pool:
            return jsonify({'message': 'Pool not found'})
        request_type = 'Training'
        pool_name = pool.pool_name
        pool_address = pool.pool_address
        pool_size = pool.size
        pool_depth = pool.depth
        pool_desc = pool.description
        pool_open_time = pool.opening_time
        pool_close_time = pool.closing_time
        pool_weekday_fee = pool.weekday_fee
        pool_weekend_fee = pool.weekend_fee
        msg = Message('Training Request', sender='easyswim123@gmail.com',
                      recipients=["easyswim123@gmail.com"])
        html_body_args = (request_type, user_fname, user_lname,
                          user_phone_number, user_email, pool_name, pool_address,
                          pool_size, pool_depth, pool_desc, pool_open_time, pool_close_time,
                          pool_weekday_fee, pool_weekend_fee)
        msg.html = html_body(*html_body_args)

        mail.send(msg)
        return jsonify({"message": "Your request was submitted, You will be contacted shortly"})
    elif str(pool_request) == 'swimming':
        pool = Pool.query.get(pool_id)
        if not pool:
            return jsonify({'message': 'Pool not found'})
        request_type = 'Swimming'
        pool_name = pool.pool_name
        pool_address = pool.pool_address
        pool_size = pool.size
        pool_depth = pool.depth
        pool_desc = pool.description
        pool_open_time = pool.opening_time
        pool_close_time = pool.closing_time
        pool_weekday_fee = pool.weekday_fee
        pool_weekend_fee = pool.weekend_fee
        msg = Message('Swim Request', sender='easyswim123@gmail.com',
                      recipients=["easyswim123@gmail.com"])
        html_body_args = (request_type, user_fname, user_lname,
                          user_phone_number, user_email, pool_name, pool_address,
                          pool_size, pool_depth, pool_desc, pool_open_time, pool_close_time,
                          pool_weekday_fee, pool_weekend_fee)
        msg.html = html_body(*html_body_args)
        mail.send(msg)
        return jsonify({"message": "Thank you for choosing to swim with us"})
    elif str(pool_request) == 'corporate':
        pool = Pool.query.get(pool_id)
        if not pool:
            return jsonify({'message': 'Pool not found'})
        request_type = 'Corporate'
        pool_name = pool.pool_name
        pool_address = pool.pool_address
        pool_size = pool.size
        pool_depth = pool.depth
        pool_desc = pool.description
        pool_open_time = pool.opening_time
        pool_close_time = pool.closing_time
        pool_weekday_fee = pool.weekday_fee
        pool_weekend_fee = pool.weekend_fee
        msg = Message('Corporate Request', sender='easyswim123@gmail.com',
                      recipients=["easyswim123@gmail.com"])
        html_body_args = (request_type, user_fname, user_lname,
                          user_phone_number, user_email, pool_name, pool_address,
                          pool_size, pool_depth, pool_desc, pool_open_time, pool_close_time,
                          pool_weekday_fee, pool_weekend_fee)
        msg.html = html_body(*html_body_args)
        mail.send(msg)
        return jsonify({"message": "Your request was submitted, You will be contacted shortly"})
    elif str(pool_request) == 'family':
        pool = Pool.query.get(pool_id)
        if not pool:
            return jsonify({'message': 'Pool not found'})
        request_type = 'Family'
        pool_name = pool.pool_name
        pool_address = pool.pool_address
        pool_size = pool.size
        pool_depth = pool.depth
        pool_desc = pool.description
        pool_open_time = pool.opening_time
        pool_close_time = pool.closing_time
        pool_weekday_fee = pool.weekday_fee
        pool_weekend_fee = pool.weekend_fee
        msg = Message('Family Request', sender='easyswim123@gmail.com',
                      recipients=["easyswim123@gmail.com"])
        html_body_args = (request_type, user_fname, user_lname,
                          user_phone_number, user_email, pool_name, pool_address,
                          pool_size, pool_depth, pool_desc, pool_open_time, pool_close_time,
                          pool_weekday_fee, pool_weekend_fee)
        msg.html = html_body(*html_body_args)
        mail.send(msg)
        return jsonify({"message": "Your request was submitted, You will be contacted shortly"})

    return jsonify({'message': "Request was unsuccessful. Something went wrong"})


def html_body(request_type, user_fname, user_lname,
              user_phone_number, user_email, pool_name, pool_address,
              pool_size, pool_depth, pool_desc, pool_opening_time,
              pool_closing_time, pool_weekday_fee, pool_weekend_fee):
    return f"""\
                    <html>
                    <head>
                    </head>
                    <body>
                        <p
                        style="
                            color: #bbc4cc; 
                            background-color: #37474f;  
                            border-radius: 5px;
                            padding-left: 5px;
                            padding-top: 10px;
                            padding-bottom: 10px;
                            "
                        >
                           A {request_type} request has been made by <b>{user_fname}  {user_lname}</b>.
                            <br>
                            <b>Phone number:</b> {user_phone_number}
                            <br>
                            <b>Email:</b> <a style="color: #eeeeee;">{user_email}</a>
                            <br>
                        </p>
                        <p
                          style="
                            color: #bbc4cc; 
                            background-color: #37474f;  
                            border-radius: 5px;
                            padding-left: 5px;
                            padding-top: 10px;
                            padding-bottom: 10px;
                            "
                        >
                            <a style="font-size: 19px; color: #eeeeee;"><b>Pool information</b></a>
                            <br>
                            Pool name: {pool_name}
                            <br>
                            Pool address: {pool_address}
                            <br>
                            Pool size: {pool_size}
                            <br>
                            Pool depth: {pool_depth}
                            <br>
                            Description: {pool_desc}
                            <br>
                            Opening time: {pool_opening_time}
                            <br>
                            Closing time: {pool_closing_time}
                            <br>
                            Weekday fee: {pool_weekday_fee}
                            <br>
                            Weekend fee: {pool_weekend_fee}
                        </p>
                    </body>
                    </html>
                    """
