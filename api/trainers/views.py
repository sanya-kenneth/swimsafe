from api.trainers import trainer_bp
from api.trainers.controllers import TrainerController
from api.auth.utilities import protected_route


trainer = TrainerController()


@trainer_bp.route('/trainers/<pool_id>', methods=['POST'])
@protected_route
def create_trainer(current_user, pool_id):
    return trainer.add_trainer(current_user, pool_id)