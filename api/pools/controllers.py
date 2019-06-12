from flask import jsonify, request, abort,\
    make_response
from api.database.db import db
from api.pools.models import Pool, Pool_packages
from api.auth.models import User
from api.pools.utilities import ValidatePools
from api.auth.utilities import validateUser
from flask import current_app as app
from flask_whooshalchemyplus import index_all
from api.subscriptions.models import Subscribe
from api.trainers.models import Trainer


validate_user = validateUser()


class PoolController:
    def __init__(self):
        pass

    def add_pool(self, current_user):
        # check if user is loggedin
        validate_user.check_user_is_loggedin(current_user)
        # check if the user is a admin
        validate_user.is_admin_user(current_user)
        data = request.get_json()
        pool_name = data.get('pool_name')
        pool_address = data.get('pool_address')
        location_lat = data.get('location_lat')
        location_long = data.get('location_long')
        opening_time = data.get('opening_time')
        closing_time = data.get('closing_time')
        size = data.get('size')
        depth = data.get('depth')
        description = data.get('description')
        weekday_fee = data.get('weekday_fee')
        weekend_fee = data.get('weekend_fee')
        available = data.get('available')
        # Initialize pool validator class
        pool_validator = ValidatePools()
        # store arguments for check_missing_fields validation method in a tupple
        field_args = (pool_name, pool_address, location_lat,
                      location_long, opening_time, closing_time, size,
                      depth,  description, weekday_fee, weekend_fee, available,)
        # store key word arguments for initializing the Pool model class
        pool_class_kwargs = dict(pool_name=pool_name, pool_address=pool_address,
                                 location_lat=location_lat, location_long=location_long,
                                 opening_time=opening_time, closing_time=closing_time,
                                 size=size, depth=depth, description=description,
                                 weekday_fee=weekday_fee, weekend_fee=weekend_fee,
                                 available=available)
        # unpack the check_missing_fields validation method
        pool_validator.check_missing_fields(*field_args)
        # validate pool name
        pool_validator.validate_pool_name(pool_name)
        # validate pool address
        pool_validator.validate_pool_address(pool_address)
        # validate pool location cordinates
        pool_validator.validate_location(location_lat, location_long)
        # check if pool exists
        pool_info = Pool.query.all()
        if pool_info:
            for pool_i in pool_info:
                if pool_i.pool_name == pool_name:
                    return jsonify({'message': 'Swimming pool already registered',
                                    'status': 400})
        # unpack the pool class with key word arguments
        new_pool = Pool(**pool_class_kwargs)
        db.session.add(new_pool)
        db.session.commit()
        return jsonify({'message': 'Swimming pool was successfuly added',
                        'status': 201})

    def fetch_all_pools(self):
        fetch_pools = Pool.query.all()
        if not fetch_pools:
            return jsonify({'message': 'There no pools registered yet',
                            'status': 404})
        pool_list = []
        pool_keys = ['pool_id', 'pool_name', 'pool_address', 'location_lat',
                     'location_long', 'opening_time', 'closing_time', 'size',
                     'depth', 'description', 'weekday_fee', 'weekend_fee',
                     'availability', 'pool_thumbnail']
        for pool_item in fetch_pools:
            pool_details = [pool_item.pool_id, pool_item.pool_name,
                            pool_item.pool_address, pool_item.location_lat,
                            pool_item.location_long, pool_item.opening_time,
                            pool_item.closing_time, pool_item.size, pool_item.depth,
                            pool_item.description, pool_item.weekday_fee,
                            pool_item.weekend_fee, pool_item.available, pool_item.pool_thumbnail]
            pool_list.append(dict(zip(pool_keys, pool_details)))
        return jsonify({'data': pool_list, 'status': 200})

    def check_id(self, id):
        """
        Checks if the provided id is a valid number by attempting to convert
        it into an integer
        """
        try:
            int(id)
        except:
            return abort(make_response(jsonify({'message': 'Pool id must be a valid number',
                                                'status': 400})))

    def fetch_one_pool(self, pool_id):
        self.check_id(pool_id)
        fetch_pool = Pool.query.get(pool_id)
        if not fetch_pool:
            return jsonify({'message': 'Swimming pool not found',
                            'status': 404})
        pool_display = {
            'pool_id': fetch_pool.pool_id,
            'pool_name': fetch_pool.pool_name,
            'pool_address': fetch_pool.pool_address,
            'location_lat': fetch_pool.location_lat,
            'location_long': fetch_pool.location_long,
            'opening_time': fetch_pool.opening_time,
            'closing_time': fetch_pool.closing_time,
            'size': fetch_pool.size,
            'depth': fetch_pool.depth,
            'description': fetch_pool.description,
            'weekday_fee': fetch_pool.weekday_fee,
            'weekdend_fee': fetch_pool.weekend_fee,
            'availability': fetch_pool.available,
            'pool_thumbnail': fetch_pool.pool_thumbnail,
        }
        return jsonify({'data': pool_display,
                        'status': 200})

    def update_field(self, db_query, field, new_value):
        """
        method updates a specific field.

        :params:
        db_query, field, new_value

        db_query => current query to fetch from the database

        field => the field to update in the database

        new_value => the new data provided by the user
        """
        if field is not None:
            setattr(db_query, field, new_value)
            db.session.commit()

    def set_initial_data(self, select_query, *args):
        """
        set data to initial data in the database if the user doesnot provide
        data on performing an update.

        :Params:

        select_query

        Also takes in *args which should be in the order below ::

        pool_name, pool_address, opening_time, closing_time, size, depth,
        description, cost, available
        """
        if not args[0]:
            select_query.pool_name = select_query.pool_name
            db.session.commit()
        if not args[1]:
            select_query.pool_address = select_query.pool_address
            db.session.commit()
        if not args[2]:
            select_query.location_lat = select_query.location_lat
            db.session.commit()
        if not args[3]:
            select_query.location_long = select_query.location_long
            db.session.commit()
        if not args[4]:
            select_query.opening_time = select_query.opening_time
            db.session.commit()
        if not args[5]:
            select_query.closing_time = select_query.closing_time
            db.session.commit()
        if not args[6]:
            select_query.size = select_query.size
            db.session.commit()
        if not args[7]:
            select_query.depth = select_query.depth
            db.session.commit()
        if not args[8]:
            select_query.description = select_query.description
            db.session.commit()

    def edit_pool_info(self, current_user, pool_id):
        # check if the user is loggedin
        validate_user.check_user_is_loggedin(current_user)
        # check if the user is an admin
        validate_user.is_admin_user(current_user)
        # check if the pool_id provided is valid
        self.check_id(pool_id)
        data = request.get_json()
        pool_name = data.get('pool_name')
        pool_address = data.get('pool_address')
        opening_time = data.get('opening_time')
        closing_time = data.get('closing_time')
        size = data.get('size')
        depth = data.get('depth')
        description = data.get('description')
        weekday_fee = data.get('weekday_fee')
        weekend_fee = data.get('weekend_fee')
        if data['pool_name']:
            print(data)
        validate_pool = ValidatePools()
        hold_pools = Pool.query.filter_by(pool_id=pool_id).first()
        if not hold_pools:
            return jsonify({'message': 'Swimmig pool not found',
                            'status': 404})
        field_tuple = (hold_pools, pool_name, pool_address,
                       opening_time, closing_time, size, depth, description,
                       weekday_fee, weekend_fee)
        self.set_initial_data(*field_tuple)
        if pool_name is not None and pool_name != "":
            validate_pool.validate_pool_name(pool_name)
            # update pool name if a value is provided by the user
            self.update_field(hold_pools, "pool_name", pool_name)
        if pool_address is not None and pool_address != "":
            validate_pool.validate_pool_address(pool_address)
            # update pool address if a value is provided by the user
            self.update_field(hold_pools, "pool_address", pool_address)
        if opening_time is not None and opening_time != "":
            # update pool opening time if a value is provided by the user
            self.update_field(hold_pools, "opening_time", opening_time)
        if closing_time is not None and closing_time != "":
            # update pool closing time if a value is provided by the user
            self.update_field(hold_pools, "closing_time", closing_time)
        if size is not None and size != "":
            # update pool size if a value is provided by the user
            self.update_field(hold_pools, "size", size)
        if depth is not None and depth != "":
            # update pool depth if a value is provided by the user
            self.update_field(hold_pools, "depth", depth)
        if description is not None and description != "":
            # update pool description if a value is provided by the user
            self.update_field(hold_pools, "description", description)
        if weekday_fee is not None and weekday_fee != "":
            # update pool weekday_fee if a value is provided by the user
            self.update_field(hold_pools, "weekday_fee", weekday_fee)
        if weekend_fee is not None and weekend_fee != "":
            # update pool weekend_fee if a value is provided by the user
            self.update_field(hold_pools, "weekend_fee", weekend_fee)
        return jsonify({'message': 'Update was successful',
                        'status': 202})

    def delete_pool_info(self, current_user, pool_id):
        # check if pool_id is valid
        self.check_id(pool_id)
        # check if the user is an admin
        validate_user.is_admin_user(current_user)
        delete_pointer = Pool.query.filter_by(pool_id=pool_id).first()
        if not delete_pointer:
            return jsonify({'message': 'Swimming pool doesnot exist',
                            'status': 404})
        db.session.delete(delete_pointer)
        db.session.commit()
        return jsonify({'message': 'Swimming pool deleted successfuly',
                        'status': 204})

    def search_pools(self):
        data = request.get_json()
        search_query = data.get('search')
        index_all(app)
        try:
            search_result = Pool.query.whoosh_search(search_query).all()
        except:
            return jsonify({'message': 'No match found', 'status': 404})
        hold = []
        keys = ["pool_id", "pool_name", "pool_address", "location_lat",
                "location_long", "opening_time", "closing_time", "size",
                "depth", "description", "weekday_fee", "weekend_fee", "availale", "pool_thumbnail"]
        for result in search_result:
            info = [result.pool_id, result.pool_name, result.pool_address,
                    result.location_lat, result.location_long, result.opening_time,
                    result.closing_time, result.size, result.depth, result.description,
                    result.weekday_fee, result.weekend_fee, result.available, result.pool_thumbnail]
            hold.append(dict(zip(keys, info)))
        return jsonify({'data': hold, 'status': 200})

    def add_package(self, pool_id):
        data = request.get_json()
        package_type = data.get("package_type")
        package_types = ['gold', 'platinum', 'silver']
        if package_type not in package_types:
            return jsonify({'message': 'Oops.. Invalid package type.'})
        pool = Pool.query.filter_by(pool_id=pool_id).first()
        if not pool:
            return jsonify({'message': 'Pool not found'})
        package_details = data.get("package_details")
        package_exists = Pool_packages.query.filter_by(
            pool_id=pool_id, package_type=package_type).first()
        if package_exists:
            setattr(package_exists, 'package_details', package_details)
            db.session.commit()
            return jsonify({'message': 'Pool package updated'})
        if not package_type or not package_details:
            return jsonify({'message': 'package type and details are required',
                            'status': 400})
        package = Pool_packages(pool_id=pool_id, package_type=package_type,
                                package_details=package_details)
        db.session.add(package)
        db.session.commit()
        return jsonify({'message': 'Pool package was created'})

    def get_package(self, pool_id, package_type):
        if not package_type:
            return jsonify({'message': 'Please specify a package type'})
        package = Pool_packages.query.filter_by(
            pool_id=pool_id, package_type=package_type).first()
        if not package:
            return jsonify({'message': 'Package not found'})
        return jsonify({'package_type': package.package_type,
                        'package_details': package.package_details,
                        'package_id': package.package_id})

    def delete_package(self, current_user, package_id):
        # check if the user is an admin
        validate_user.is_admin_user(current_user)
        delete_package = Pool_packages.query.filter_by(
            package_id=package_id).first()
        if not delete_package:
            return jsonify({'message': 'Pool package doesnot exist',
                            'status': 404})
        db.session.delete(delete_package)
        db.session.commit()
        return jsonify({'message': 'Swimming pool package deleted successfuly',
                        'status': 204})

    def statistics(self, current_user, pool_id):
        # check if the user is an admin
        validate_user.is_admin_user(current_user)
        # number of trainers
        trainers = Trainer.query.filter_by(pool_id=pool_id).all()
        if trainers:
            num_trainers = len(trainers)
        else:
            num_trainers = 0
        subscribers = Subscribe.query.filter_by(pool_id=pool_id).all()
        if subscribers:
            num_subscribers = len(subscribers)
        else:
            num_subscribers = 0
        return jsonify({'Trainers': num_trainers,
                        'Subscribers': num_subscribers})
