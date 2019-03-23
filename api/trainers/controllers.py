from api.database.db import db
from flask import jsonify, request, abort
from api.auth.utilities import validateUser
from api.trainers.utilities import ValidateTrainer
from api.trainers.models import Trainer
from api.pools.models import Pool


user_valid = validateUser()
trainer_validate = ValidateTrainer()


class TrainerController:
    def __init__(self):
        pass


    def add_trainer(self, current_user, pool_id):
        user_valid.check_user_is_loggedin(current_user)
        # user_valid.is_admin_user(current_user)
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
                print(pool.pool_id)
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
                                return jsonify({'error': 'Trainer already exists',\
                                                'status': 400}), 400
                    db.session.add(add_trainer)
                    db.session.commit()
                    return jsonify({'message': 'Trainer was successfuly added',
                                    'status': 201}), 201
        return jsonify({'error': "Swimming pool was not found",
                        'status': 404}), 404
