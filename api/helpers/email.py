from flask_mail import Mail, Message
from flask import request, jsonify, current_app as app
from api.pools.models import Pool


def send_email(current_user, pool_id):
    mail = Mail(app)
    data = request.get_json()
    pool_request = data.get("pool_request")
    if str(pool_request) == 'training':
        pool = Pool.query.get(pool_id)
        if not pool:
            return jsonify({'message': 'Pool not found'})
        msg = Message('Training Request', sender='sanyakenneth@gmail.com',
                      recipients=[current_user.email])
        msg.body = f'A training request has been made by {current_user.firstname}  {current_user.lastname}.\
                  \nPhone number: 0{current_user.phone_number}.\
                  \nEmail: {current_user.email} \
                  \n  \
                  \n******* Pool information ********\
                  \n \
                  \nPool name: {pool.pool_name}\
                  \nPool address: {pool.pool_address}\
                  \nPool size: {pool.size}\
                  \nPool depth: {pool.depth}\
                  \nDescription: {pool.description}\
                  \nOpening time: {pool.opening_time}\
                  \nClosing time: {pool.closing_time}\
                  \nWeekday fee: {pool.weekday_fee}\
                  \nWeekend fee: {pool.weekend_fee}'
        mail.send(msg)
        return jsonify({"message": "Your request was submitted, You will be contacted within 24hrs"})
        return
    elif str(pool_request) == 'swimming':
        pool = Pool.query.get(pool_id)
        msg = Message('Swim Request', sender='sanyakenneth@gmail.com',
                      recipients=[current_user.email])
        msg.body = f'A swim request has been made by {current_user.firstname}  {current_user.lastname}.\
                  \nPhone number: 0{current_user.phone_number}.\
                  \nEmail: {current_user.email} \
                  \n  \
                  \n******* Pool information ********\
                  \n \
                  \nPool name: {pool.pool_name}\
                  \nPool address: {pool.pool_address}\
                  \nPool size: {pool.size}\
                  \nPool depth: {pool.depth}\
                  \nDescription: {pool.description}\
                  \nOpening time: {pool.opening_time}\
                  \nClosing time: {pool.closing_time}\
                  \nWeekday fee: {pool.weekday_fee}\
                  \nWeekend fee: {pool.weekend_fee}'
        mail.send(msg)
        return jsonify({"message": "Your request was submitted, You will be contacted within 24hrs"})
    return jsonify({'message': "Request was unsuccessful. Something went wrong"})
