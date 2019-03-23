from api.pools import pools_bp
from api.pools.controllers import PoolController
from api.auth.utilities import protected_route


pool = PoolController()

@pools_bp.route('/pools', methods=['POST'])
@protected_route
def add_swimming_pool(current_user):
    return pool.add_pool(current_user)


@pools_bp.route('/pools', methods=['GET'])
@protected_route
def get_all_pools(current_user):
    return pool.fetch_all_pools()


@pools_bp.route('/pools/<pool_id>', methods=['GET'])
@protected_route
def get_one_pool(current_user, pool_id):
    return pool.fetch_one_pool(pool_id)


@pools_bp.route('/pools/<pool_id>/update', methods=['PUT'])
@protected_route
def update_pool_info(current_user, pool_id):
    return pool.edit_pool_info(current_user, pool_id)


@pools_bp.route('/pools/<pool_id>', methods=['DELETE'])
@protected_route
def delete_pool(current_user, pool_id):
    return pool.delete_pool_info(current_user, pool_id)