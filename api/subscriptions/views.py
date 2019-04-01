from api.subscriptions import subs_bp
from api.auth.utilities import protected_route
from api.subscriptions.controllers import subscriptionController


subscribe_obj = subscriptionController()


@subs_bp.route('/pools/<pool_id>/subscribe', methods=['PUT'])
@protected_route
def subscribe(current_user, pool_id):
    return subscribe_obj.subscribe_to_pool(current_user, pool_id)


@subs_bp.route('/users/subscriptions', methods=['GET'])
@protected_route
def fetch_subscriptions(current_user):
    return subscribe_obj.get_subscriptions(current_user)


@subs_bp.route('/pools/subscribers/<pool_id>', methods=['GET'])
@protected_route
def fetch_subscribers(current_user, pool_id):
    return subscribe_obj.get_subscribers(current_user, pool_id)