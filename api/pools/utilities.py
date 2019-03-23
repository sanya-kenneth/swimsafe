from flask import jsonify, make_response, abort


class ValidatePools:
    def __init__(self):
        pass

    @staticmethod
    def response(response_message, status):
        abort(make_response(jsonify(response_message), status))


    def validate_pool_name(self, pool_name):
        if not isinstance(pool_name, str):
            response = {'error': 'Pool name is not valid',
                        'status': 400}
            response_status = 400
            ValidatePools.response(response, response_status)


    def validate_pool_address(self, pool_address):
        if not isinstance(pool_address, str):
            response = {'error': 'Pool address is not valid',
                        'status': 400}
            response_status = 400
            ValidatePools.response(response, response_status)


    def validate_location(self, lat_value, long_value):
        if not isinstance(lat_value, float):
            response = {'error': 'Location Lat cordinate is not valid',
                        'status': 400}
            response_status = 400
            ValidatePools.response(response, response_status)
        if not isinstance(long_value, float):
            response = {'error': 'Location Long cordinate is not valid',
                        'status': 400}
            response_status = 400
            ValidatePools.response(response, response_status)

    def check_missing_fields(self, *args):
        """
        params:
        pool_name, pool_address, lat, long,
        opening_time, closing_time, size, depth,
        description, cost, available
        """
        if not args[0]:
            response = {'error': 'Pool name field is missing or empty',
                        'status': 400}
            response_status = 400
            ValidatePools.response(response, response_status)
        if not args[1]:
            response = {'error': 'Pool address field is missing or empty',
                        'status': 400}
            response_status = 400
            ValidatePools.response(response, response_status)
        if not args[2]:
            response = {'error': 'Location lattitude cordinate field is missing or empty',
                        'status': 400}
            response_status = 400
            ValidatePools.response(response, response_status)
        if not args[3]:
            response = {'error': 'Location longitude field is missing or empty',
                        'status': 400}
            response_status = 400
            ValidatePools.response(response, response_status)
        if not args[4]:
            response = {'error': 'Pool opening time field is missing or empty',
                        'status': 400}
            response_status = 400
            ValidatePools.response(response, response_status)
        if not args[5]:
            response = {'error': 'Pool closing time field is missing or empty',
                        'status': 400}
            response_status = 400
            ValidatePools.response(response, response_status)
        if not args[6]:
            response = {'error': 'Pool size field is missing or empty',
                        'status': 400}
            response_status = 400
            ValidatePools.response(response, response_status)
        if not args[7]:
            response = {'error': 'Pool depth field is missing or empty',
                        'status': 400}
            response_status = 400
            ValidatePools.response(response, response_status)
        if not args[8]:
            response = {'error': 'Pool description field is missing or empty',
                        'status': 400}
            response_status = 400
            ValidatePools.response(response, response_status)
        if not args[9]:
            response = {'error': 'Pool cost field is missing or empty',
                        'status': 400}
            response_status = 400
            ValidatePools.response(response, response_status)

        if not args[10]:
            response = {'error': 'Pool availability field is missing or empty',
                        'status': 400}
            response_status = 400
            ValidatePools.response(response, response_status)
