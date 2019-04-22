from api.rating_system import rate_bp
from api.auth.utilities import protected_route
from api.rating_system.controllers import rate_trainer,\
    retrieve_trainer_rating


@rate_bp.route('/rate/<trainer_id>', methods=['POST'])
@protected_route
def make_rating(current_user, trainer_id):
    return rate_trainer(current_user, trainer_id)


@rate_bp.route('/rate/<trainer_id>', methods=['GET'])
@protected_route
def fetch_trainer_rating(current_user, trainer_id):
    return retrieve_trainer_rating(current_user, trainer_id)
