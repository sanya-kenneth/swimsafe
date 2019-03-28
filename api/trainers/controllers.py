from api.database.db import db
from flask import jsonify, request, abort
from api.auth.utilities import validateUser
from api.trainers.utilities import ValidateTrainer
from api.trainers.models import Trainer
from api.pools.models import Pool
import re


user_valid = validateUser()
trainer_validate = ValidateTrainer()


class TrainerController:
    def __init__(self):
        pass


    def add_trainer(self, current_user, pool_id):
        user_valid.check_user_is_loggedin(current_user)
        user_valid.is_admin_user(current_user)
        data = request.get_json()
        trainer_firstname = data.get("firstname")
        trainer_lastname = data.get("lastname")
        working_time = data.get("working_time")
        trainer_description = data.get("description")
        trainer_available = data.get("avaliable")
        trainer_validate.check_missing_data(trainer_firstname, trainer_lastname,\
            working_time, trainer_description, trainer_available)
        trainer_validate.validate_name(trainer_firstname)
        trainer_validate.validate_name(trainer_lastname)
        trainer_validate.validate_description(trainer_description)
        get_pools = Pool.query.all()
        if get_pools:
            for pool in get_pools:
                if int(pool.pool_id) == int(pool_id):
                    # Add trainer
                    add_trainer = Trainer(first_name=trainer_firstname, last_name=trainer_lastname,\
                        working_time=working_time, description=trainer_description,\
                        available=trainer_available, pool_id=pool_id)
                    get_trainer = Trainer.query.all()
                    if get_trainer:
                        for trainer_individual in get_trainer:
                            if trainer_individual.first_name == trainer_firstname and\
                                trainer_individual.last_name == trainer_lastname and\
                                trainer_individual.description == trainer_description:
                                return jsonify({'message': 'Trainer already exists',\
                                                'status': 400}), 400
                    db.session.add(add_trainer)
                    db.session.commit()
                    return jsonify({'message': 'Trainer was successfuly added',
                                    'status': 201}), 201
        return jsonify({'message': "Swimming pool was not found",
                        'status': 404}), 404

    def edit_trainer_info(self, current_user, trainer_id):
        user_valid.check_user_is_loggedin(current_user)
        user_valid.is_admin_user(current_user)
        data = request.get_json()
        trainer_f_name = data.get("firstname")
        trainer_l_name = data.get("lastname")
        working_time = data.get("working_time")
        description = data.get("description")
        available = data.get("available")
        # pool_id = data["pool_id"]
        trainer_query = Trainer.query.filter_by(trainer_id=trainer_id).first()
        if not trainer_query:
            return jsonify({'message': 'Trainer not registered with us',
                            'status': 404}), 404
        if trainer_f_name is not None:
            if not isinstance(trainer_f_name, str) or\
                re.search(r'[\s]', trainer_f_name) or\
                trainer_f_name == "":
                return jsonify({'message': 'firstname must be a string with atleast 4 characters',
                                'status': 400}), 400
            setattr(trainer_query, "first_name", trainer_f_name)
            db.session.commit()
        else:
            trainer_query.first_name = trainer_query.first_name
            db.session.commit()
        if trainer_l_name is not None:
            if not isinstance(trainer_l_name, str) or\
                re.search(r'[\s]', trainer_l_name) or\
                trainer_l_name == "":
                return jsonify({'message': 'lastname must be a string with atleast 4 characters',
                                'status': 400}), 400
            setattr(trainer_query, "last_name", trainer_l_name)
            db.session.commit()
        else:
            trainer_query.last_name = trainer_query.last_name
            db.session.commit()
        if working_time is not None:
            setattr(trainer_query, "working_time", working_time)
            db.session.commit()
        else:
            trainer_query.working_time = trainer_query.working_time
            db.session.commit()
        if description is not None:
            setattr(trainer_query, "description", description)
            db.session.commit()
        else:
            trainer_query.description = trainer_query.description
            db.session.commit()
        if available is not None:
            setattr(trainer_query, "available", available)
            db.session.commit()
        else:
            trainer_query.available = trainer_query.available
            db.session.commit()
        return jsonify({'message': 'Trainer information updated successfuly',
                        'status': 202}), 202


    def delete_trainer(self, current_user, trainer_id):
        user_valid.check_user_is_loggedin(current_user)
        user_valid.is_admin_user(current_user)
        try:
            int(trainer_id)
        except:
            return jsonify({'message': 'Trainer id must be a valid number',
                            'status': 400}), 400
        remove_trainer = Trainer.query.filter_by(trainer_id=trainer_id).first()
        if not remove_trainer:
            return jsonify({'message': 'Trainer not found',
                            'status': 404}), 404
        db.session.delete(remove_trainer)
        db.session.commit()
        return jsonify({'message': 'Trainer information was deleted',
                        'status': 204}), 204


    def get_one_trainer(self, current_user, trainer_id):
        user_valid.check_user_is_loggedin(current_user)
        try:
            int(trainer_id)
        except:
            return jsonify({'message': 'Trainer id must be a valid number',
                            'status': 400}), 400
        get_trainer = Trainer.query.filter_by(trainer_id=trainer_id).first()
        if not get_trainer:
            return jsonify({'message': 'Trainer not found', 'status': 404}), 404
        trainer_data = dict(
            trainer_id = get_trainer.trainer_id,
            first_name = get_trainer.first_name,
            last_name = get_trainer.last_name,
            working_time = get_trainer.working_time,
            description = get_trainer.description,
            availability = get_trainer.available,
            pool_id = get_trainer.pool_id
        )
        return jsonify({'data': trainer_data, 'status': 200}), 200


    def get_trainers(self, current_user):
        user_valid.check_user_is_loggedin(current_user)
        get_trainers = Trainer.query.all()
        if not get_trainers:
            return jsonify({'message': 'There no trainers yet',
                            'status': 404}), 404
        trainer_list = []
        trainer_keys = ['trainer_id', 'firstname', 'lastname', 'working_time',
                        'description', 'availability', 'pool_id']
        for trainer_item in get_trainers:
            trainer_details = [trainer_item.trainer_id, trainer_item.first_name,
                               trainer_item.last_name, trainer_item.working_time,
                               trainer_item.description, trainer_item.available,
                               trainer_item.pool_id]
            trainer_list.append(dict(zip(trainer_keys, trainer_details)))
        return jsonify({'data': trainer_list, 'status': 200}), 200
