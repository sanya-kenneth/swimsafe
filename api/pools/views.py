from api.pools import pools_bp
from api.pools.controllers import PoolController
from api.auth.utilities import protected_route
from api.helpers.upload import upload_file
from api.helpers.email import send_email


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


@pools_bp.route('/pools/search', methods=['POST'])
@protected_route
def search_for_pools(current_user):
    return pool.search_pools()


@pools_bp.route('/pools/upload/<pool_id>', methods=['POST'])
@protected_route
def upload_pic(current_user, pool_id):
    return upload_file(current_user, pool_id=pool_id, table='pools')


@pools_bp.route('/pools/request/<pool_id>', methods=['POST'])
@protected_route
def pool_request(current_user, pool_id):
    return send_email(current_user, pool_id)


@pools_bp.route('/pools/packages/<pool_id>', methods=['POST'])
@protected_route
def add_packages(current_user, pool_id):
    return pool.add_package(pool_id)


@pools_bp.route('/pools/packages/<pool_id>/platinum', methods=['GET'])
@protected_route
def get_package(current_user, pool_id):
    return pool.get_package(pool_id, 'platinum')


@pools_bp.route('/pools/packages/<pool_id>/silver', methods=['GET'])
@protected_route
def get_package_silver(current_user, pool_id):
    return pool.get_package(pool_id, 'silver')


@pools_bp.route('/pools/packages/<pool_id>/gold', methods=['GET'])
@protected_route
def get_package_gold(current_user, pool_id):
    return pool.get_package(pool_id, 'gold')


@pools_bp.route('/pools/packages/<package_id>/delete', methods=['DELETE'])
@protected_route
def delete_package(current_user, package_id):
    return pool.delete_package(current_user, package_id)


@pools_bp.route('/pools/<pool_id>/statistics', methods=['GET'])
@protected_route
def statistics(current_user, pool_id):
    return pool.statistics(current_user, pool_id)
