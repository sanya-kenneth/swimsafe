from flask import jsonify, request, abort,\
    make_response
from api.database.db import db
from api.auth.models import User
from api.children_pool.models import Children_Pool
from api.pools.utilities import ValidatePools
from api.auth.utilities import validateUser
from flask import current_app as app
import re


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


def fetch_all_children_pools(pool_id):
    fetch_children_pools = Children_Pool.query.filter_by(pool_id=pool_id).all()
    if not fetch_children_pools:
        return jsonify({'message': 'There no pools registered yet',
                        'status': 404})
    children_pool_list = []
    children_pool_keys = ['child_pool_id', 'child_pool_name', 'size',
                          'depth', 'description', 'weekday_fee', 'weekend_fee',
                          'availability', 'thumbnail', 'pool_id']
    for child_pool_item in fetch_children_pools:
        child_pool_details = [child_pool_item.child_pool_id, child_pool_item.name,
                              child_pool_item.size, child_pool_item.depth,
                              child_pool_item.description, child_pool_item.weekday_fee,
                              child_pool_item.weekend_fee, child_pool_item.available,
                              child_pool_item.thumbnail, child_pool_item.pool_id]
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
        'child_pool_name': fetch_child_pool.name,
        'size': fetch_child_pool.size,
        'depth': fetch_child_pool.depth,
        'description': fetch_child_pool.description,
        'weekday_fee': fetch_child_pool.weekday_fee,
        'weekdend_fee': fetch_child_pool.weekend_fee,
        'availability': fetch_child_pool.available,
        'thumnail': fetch_child_pool.thumbnail,
        'pool_id': fetch_child_pool.pool_id
    }
    return jsonify({'data': child_pool_display,
                    'status': 200})


def edit_children_pool(current_user, pool_id):
    validate_user.check_user_is_loggedin(current_user)
    validate_user.is_admin_user(current_user)
    data = request.get_json()
    name = data.get('name')
    size = data.get("size")
    depth = data.get("depth")
    description = data.get("description")
    weekday_fee = data.get("weekday_fee")
    weekend_fee = data.get("weekend_fee")
    available = data.get("available")
    childpool_query = Children_Pool.query.filter_by(
        child_pool_id=pool_id).first()
    if not childpool_query:
        return jsonify({'message': 'Children pool not registered with us',
                        'status': 404})
    if name is not None:
        if name != "":
            setattr(childpool_query, "name", name)
            db.session.commit()
        else:
            childpool_query.name = childpool_query.name
            db.session.commit()
    if size is not None:
        if size != "":
            setattr(childpool_query, "size", size)
            db.session.commit()
        else:
            childpool_query.size = childpool_query.size
            db.session.commit()
    if depth is not None and depth != "":
        setattr(childpool_query, "depth", depth)
        db.session.commit()
    else:
        childpool_query.depth = childpool_query.depth
        db.session.commit()
    if description is not None and description != "":
        setattr(childpool_query, "description", description)
        db.session.commit()
    else:
        childpool_query.description = childpool_query.description
        db.session.commit()
    if available is not None and available != "":
        setattr(childpool_query, "available", available)
        db.session.commit()
    else:
        childpool_query.available = childpool_query.available
        db.session.commit()
    if weekday_fee is not None and weekday_fee != "":
        setattr(childpool_query, "weekday_fee", weekday_fee)
        db.session.commit()
    else:
        childpool_query.weekday_fee = childpool_query.weekday_fee
        db.session.commit()
    if weekend_fee is not None and weekend_fee != "":
        setattr(childpool_query, "weekend_fee", weekend_fee)
        db.session.commit()
    else:
        childpool_query.weekend_fee = childpool_query.weekend_fee
        db.session.commit()
    return jsonify({'message': 'Children pool information updated successfuly',
                    'status': 202})


def delete_child_pool(current_user, pool_id):
    validate_user.check_user_is_loggedin(current_user)
    validate_user.is_admin_user(current_user)
    try:
        int(pool_id)
    except:
        return jsonify({'message': 'Children pool id must be a valid number',
                        'status': 400})
    remove_child_pool = Children_Pool.query.filter_by(
        child_pool_id=pool_id).first()
    if not remove_child_pool:
        return jsonify({'message': 'Children\'s pool not found',
                        'status': 404})
    db.session.delete(remove_child_pool)
    db.session.commit()
    return jsonify({'message': 'Children\'s pool was deleted',
                    'status': 204})
