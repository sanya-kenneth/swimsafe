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
    
    def save(self):
        try:
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            return jsonify({'message': f'{e}'}), 400

    def add_trainer(self, current_user, pool_id):
        user_valid.check_user_is_loggedin(current_user)
        user_valid.is_admin_user(current_user)
        data = request.get_json()
        trainer_firstname = data.get("firstname")
        trainer_lastname = data.get("lastname")
        working_time = data.get("working_time")
        trainer_description = data.get("description")
        trainer_available = data.get("avaliable")
        trainer_contact = data.get("trainer_contact")
        trainer_validate.check_missing_data(trainer_firstname, trainer_lastname,
                                            working_time, trainer_description, trainer_available)
        trainer_validate.validate_name(trainer_firstname)
        trainer_validate.validate_name(trainer_lastname)
        trainer_validate.validate_description(trainer_description)
        get_pools = Pool.query.all()
        if get_pools:
            for pool in get_pools:
                if int(pool.pool_id) == int(pool_id):
                    # Add trainer
                    add_trainer = Trainer(first_name=trainer_firstname, last_name=trainer_lastname,
                                          working_time=working_time, description=trainer_description,
                                          available=trainer_available, pool_id=pool_id,
                                          trainer_contact=trainer_contact)
                    get_trainer = Trainer.query.all()
                    if get_trainer:
                        for trainer_individual in get_trainer:
                            if trainer_individual.first_name == trainer_firstname and\
                                    trainer_individual.last_name == trainer_lastname and\
                                    trainer_individual.description == trainer_description:
                                return jsonify({'message': 'Trainer already exists',
                                                'status': 400})
                    db.session.add(add_trainer)
                    self.save()
                    return jsonify({'message': 'Trainer was successfuly added',
                                    'status': 201})
        return jsonify({'message': "Swimming pool was not found",
                        'status': 404})

    def edit_trainer_info(self, current_user, trainer_id):
        user_valid.check_user_is_loggedin(current_user)
        user_valid.is_admin_user(current_user)
        data = request.get_json()
        trainer_f_name = data.get("firstname")
        trainer_l_name = data.get("lastname")
        working_time = data.get("working_time")
        trainer_contact = data.get("trainer_contact")
        description = data.get("description")
        available = data.get("available")
        trainer_query = Trainer.query.filter_by(trainer_id=trainer_id).first()
        if not trainer_query:
            return jsonify({'message': 'Trainer not registered with us',
                            'status': 404})
        if trainer_f_name is not None:
            if not re.search(r'[\s]', trainer_f_name) and trainer_f_name != "":
                setattr(trainer_query, "first_name", trainer_f_name)
                self.save()
            else:
                trainer_query.first_name = trainer_query.first_name
                self.save()
        if trainer_l_name is not None:
            if not re.search(r'[\s]', trainer_l_name) and\
                    trainer_l_name != "":
                setattr(trainer_query, "last_name", trainer_l_name)
                self.save()
            else:
                trainer_query.last_name = trainer_query.last_name
                self.save()
        if working_time is not None and working_time != "":
            setattr(trainer_query, "working_time", working_time)
            self.save()
        else:
            trainer_query.working_time = trainer_query.working_time
            self.save()
        if description is not None and description != "":
            setattr(trainer_query, "description", description)
            self.save()
        else:
            trainer_query.description = trainer_query.description
            self.save()
        if available is not None and available != "":
            setattr(trainer_query, "available", available)
            self.save()
        else:
            trainer_query.available = trainer_query.available
            self.save()
        if trainer_contact is not None and trainer_contact != "":
            setattr(trainer_query, "trainer_contact", trainer_contact)
            self.save()
        else:
            trainer_query.trainer_contact = trainer_query.trainer_contact
            self.save()
        return jsonify({'message': 'Trainer information updated successfuly',
                        'status': 202})

    def delete_trainer(self, current_user, trainer_id):
        user_valid.check_user_is_loggedin(current_user)
        user_valid.is_admin_user(current_user)
        try:
            int(trainer_id)
        except:
            return jsonify({'message': 'Trainer id must be a valid number',
                            'status': 400})
        remove_trainer = Trainer.query.filter_by(trainer_id=trainer_id).first()
        if not remove_trainer:
            return jsonify({'message': 'Trainer not found',
                            'status': 404})
        db.session.delete(remove_trainer)
        db.session.commit()
        return jsonify({'message': 'Trainer information was deleted',
                        'status': 204})

    def get_one_trainer(self, trainer_id):
        try:
            int(trainer_id)
        except:
            return jsonify({'message': 'Trainer id must be a valid number',
                            'status': 400}), 400
        get_trainer = Trainer.query.filter_by(trainer_id=trainer_id).first()
        if not get_trainer:
            return jsonify({'message': 'Trainer not found', 'status': 404})
        trainer_data = dict(
            trainer_id=get_trainer.trainer_id,
            first_name=get_trainer.first_name,
            last_name=get_trainer.last_name,
            trainer_contact=get_trainer.trainer_contact,
            working_time=get_trainer.working_time,
            description=get_trainer.description,
            availability=get_trainer.available,
            pool_id=get_trainer.pool_id,
            trainer_img=get_trainer.trainer_img
        )
        return jsonify({'data': trainer_data, 'status': 200})

    def get_trainers(self):
        get_trainers = Trainer.query.all()
        if not get_trainers:
            return jsonify({'message': 'There no trainers yet',
                            'status': 404})
        trainer_list = []
        trainer_keys = ['trainer_id', 'first_name', 'last_name', 'working_time',
                        'trainer_contact', 'description', 'availability', 'pool_id',
                        'trainer_img']
        for trainer_item in get_trainers:
            trainer_details = [trainer_item.trainer_id, trainer_item.first_name,
                               trainer_item.last_name, trainer_item.working_time,
                               trainer_item.trainer_contact, trainer_item.description,
                               trainer_item.available, trainer_item.pool_id,
                               trainer_item.trainer_img]
            trainer_list.append(dict(zip(trainer_keys, trainer_details)))
        return jsonify({'data': trainer_list, 'status': 200})

    def get_trainers_attached_to_pool(self, pool_id):
        """
        method returns all trainers who are attached to a given swimming
        pool
        """
        trainers_fetched = Trainer.query.filter_by(pool_id=pool_id).all()
        if not trainers_fetched:
            return jsonify({'message': 'No trainers found for that swimming pool',
                            'status': 404})
        result_list = []
        t_keys = ['trainer_id', 'first_name', 'last_name', 'working_time',
                  'trainer_contact', 'description', 'availability', 'pool_id',
                  'trainer_img']
        for individual_trainer in trainers_fetched:
            t_details = [individual_trainer.trainer_id, individual_trainer.first_name,
                         individual_trainer.last_name, individual_trainer.working_time,
                         individual_trainer.trainer_contact, individual_trainer.description,
                         individual_trainer.available, individual_trainer.pool_id,
                         individual_trainer.trainer_img]
            result_list.append(dict(zip(t_keys, t_details)))
        return jsonify({'data': result_list, 'status': 200})
