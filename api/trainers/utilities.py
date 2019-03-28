from flask import abort, make_response, jsonify


class ValidateTrainer:
    def __init__(self):
        pass


    def validate_name(self, name):
        if not isinstance(name, str):
            abort(make_response(jsonify({'message': 'firstname or lastname must be a string',
                                         'status': 400}), 400))


    def validate_description(self, description):
        if not isinstance(description, str):
            abort(make_response(jsonify({'message': 'Description must be a string',
                                         'status': 400}), 400))


    def check_missing_data(self, firstname, lastname, working_time, 
                           description, available):
        if not firstname:
            abort(make_response(jsonify({'message': 'firstname is missing',
                                         'status': 400}), 400))
        if not lastname:
            abort(make_response(jsonify({'message': 'lastname is missing',
                                         'status': 400}), 400))
        if not working_time:
            abort(make_response(jsonify({'message': 'working time is required',
                                         'status': 400}), 400))
        if not description:
            abort(make_response(jsonify({'message': 'trainer description is required',
                                         'status': 400}), 400))
            