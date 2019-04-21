from flask import jsonify, request, abort,\
    make_response
from api.database.db import db
from api.auth.models import User
from api.children_pool.models import Children_Pool
from api.pools.utilities import ValidatePools
from api.auth.utilities import validateUser
from flask import current_app as app


validate_user = validateUser()


def add_children_pool(current_user, pool_id):
    # check if user is loggedin
    validate_user.check_user_is_loggedin(current_user)
    # check if the user is a admin
    validate_user.is_admin_user(current_user)
    data = request.get_json()
    name = data.get('name')
    size = data.get('size')
    depth = data.get('depth')
    description = data.get('description')
    weekday_fee = data.get('weekday_fee')
    weekend_fee = data.get('weekend_fee')
    available = data.get('available')
    # Initialize pool validator class
    pool_validator = ValidatePools()
    # store key word arguments for initializing the Pool model class
    children_pool_class_kwargs = dict(name=name, size=size,
                                      depth=depth, description=description,
                                      weekday_fee=weekday_fee, weekend_fee=weekend_fee,
                                      available=available, pool_id=pool_id)
    # validate pool name
    pool_validator.validate_pool_name(name)
    # check if pool exists
    child_pool_info = Children_Pool.query.all()
    if child_pool_info:
        for child_pool_i in child_pool_info:
            if child_pool_i.name == name:
                return jsonify({'message': 'Swimming pool already registered',
                                'status': 400})
    # unpack the pool class with key word arguments
    new_children_pool = Children_Pool(**children_pool_class_kwargs)
    db.session.add(new_children_pool)
    db.session.commit()
    return jsonify({'message': 'Swimming pool was successfuly added',
                    'status': 201})


def fetch_all_children_pools():
    fetch_children_pools = Children_Pool.query.all()
    if not fetch_children_pools:
        return jsonify({'message': 'There no pools registered yet',
                        'status': 404})
    children_pool_list = []
    children_pool_keys = ['child_pool_id', 'name', 'size',
                          'depth', 'description', 'weekday_fee', 'weekend_fee',
                          'availability', 'thumbnail']
    for child_pool_item in fetch_children_pools:
        child_pool_details = [child_pool_item.child_pool_id, child_pool_item.name,
                              child_pool_item.size, child_pool_item.depth,
                              child_pool_item.description, child_pool_item.weekday_fee,
                              child_pool_item.weekend_fee, child_pool_item.available,
                              child_pool_item.thumbnail]
        children_pool_list.append(
            dict(zip(children_pool_keys, child_pool_details)))
    return jsonify({'data': children_pool_list, 'status': 200})


def check_id(id):
    """
    Checks if the provided id is a valid number by attempting to convert
    it into an integer
    """
    try:
        int(id)
    except:
        return abort(make_response(jsonify({'message': 'Pool id must be a valid number',
                                            'status': 400})))


def fetch_one_children_pool_attached_main_pool(pool_id):
    check_id(pool_id)
    fetch_child_pool = Children_Pool.query.get(pool_id)
    if not fetch_child_pool:
        return jsonify({'message': 'Swimming pool not found',
                        'status': 404})
    child_pool_display = {
        'child_pool_id': fetch_child_pool.child_pool_id,
        'pool_name': fetch_child_pool.name,
        'size': fetch_child_pool.size,
        'depth': fetch_child_pool.depth,
        'description': fetch_child_pool.description,
        'weekday_fee': fetch_child_pool.weekday_fee,
        'weekdend_fee': fetch_child_pool.weekend_fee,
        'availability': fetch_child_pool.available,
        'thumnail': fetch_child_pool.thumbnail
    }
    return jsonify({'data': child_pool_display,
                    'status': 200})
