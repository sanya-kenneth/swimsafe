from api.children_pool import children_bp
from api.auth.utilities import protected_route
from api.children_pool.controllers import add_children_pool,\
    fetch_all_children_pools, fetch_one_children_pool_attached_main_pool


@children_bp.route('/children_pools/<pool_id>', methods=['POST'])
@protected_route
def add_children_swimming_pool(current_user, pool_id):
    return add_children_pool(current_user, pool_id)


@children_bp.route('/<pool_id>/children_pools', methods=['GET'])
@protected_route
def get_children_swimming_pools(current_user, pool_id):
    return fetch_all_children_pools(pool_id)


@children_bp.route('/children_pools/<pool_id>', methods=['GET'])
@protected_route
def get_one_children_swimming_pool(current_user, pool_id):
    return fetch_one_children_pool_attached_main_pool(pool_id)
