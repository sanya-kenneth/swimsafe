from api.subscriptions.models import Subscribe
from api.pools.models import Pool
from api.auth.models import User
from api.auth.utilities import validateUser
from api.database.db import db
from flask import jsonify


valid_user = validateUser()


class subscriptionController:
    def __init__(self):
        pass


    def subscribe_to_pool(self, current_user, pool_id):
            """
            method enables a user to subscribe
            to a swimming pool
            """
            valid_user.check_user_is_loggedin(current_user)
            if current_user.account_type == "admin":
                return jsonify({'message': 'You are not allowed to perform this action',
                                'status': 403}), 403
            # Get the pool to add a subscription for
            pool_to_subscribe = Pool.query.filter_by(pool_id=pool_id).first()
            if not pool_to_subscribe:
                return jsonify({'message': 'Swimming pool not found',
                                'status': 404}), 404
            # Get the user who is going to make the subscribe
            save_user = User.query.filter_by(user_id=current_user.user_id).first()
            # generate subscription name
            subs_name = f'{save_user.user_id} linked to {pool_to_subscribe.pool_id}'
            # get subscriptions
            subs = Subscribe.query.all()
            for sub in subs:
                if sub.sub_name == subs_name:
                    return jsonify({'message': 'You are already subscribed to this swimming pool',
                                    'status': 400}), 400
            # make the subscription
            add_subscription = Subscribe(user_id=save_user.user_id,\
                pool_id=pool_to_subscribe.pool_id, sub_name=subs_name)
            # Commit changes to the database
            db.session.add(add_subscription)
            db.session.commit()
            return jsonify({'message': 'Your subscription was successfuly made', 
                            'status': 202}), 202


    def get_subscriptions(self, current_user):
        """
        returns all pools a user is subscribed
        to.
        """
        valid_user.check_user_is_loggedin(current_user)
        if current_user.account_type == "admin":
                return jsonify({'message': 'You are not allowed to perform this action',
                                'status': 403}), 403
        user_pools = Subscribe.query.filter_by(user_id=current_user.user_id)
        pool_keys = ['pool_id', 'pool_name', 'pool_address', 'location_lat',
                     'location_long', 'opening_time', 'closing_time', 'size',
                     'depth', 'description', 'cost', 'availability']
        hold_subs = []
        if user_pools:
            for sub_pool in user_pools:
                get_pool = Pool.query.filter_by(pool_id=sub_pool.pool_id).first()
                pool_info = [get_pool.pool_id, get_pool.pool_name, get_pool.pool_address,
                             get_pool.location_lat, get_pool.location_long, get_pool.opening_time,
                             get_pool.closing_time, get_pool.size, get_pool.depth,
                             get_pool.description, get_pool.cost, get_pool.available]
                hold_subs.append(dict(zip(pool_keys, pool_info)))
            return jsonify({'data': hold_subs, 'status': 200}), 200
        return jsonify({'message': 'No subscriptions found', 'status': 404}), 404


    def get_subscribers(self, current_user, pool_id):
        """
        returns all users who have subscribed to a
        swimming pool
        """
        pass