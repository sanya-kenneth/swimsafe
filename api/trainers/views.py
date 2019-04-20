from api.trainers import trainer_bp
from api.trainers.controllers import TrainerController
from api.auth.utilities import protected_route
from api.helpers.upload import upload_file


trainer = TrainerController()


@trainer_bp.route('/trainers/<pool_id>', methods=['POST'])
@protected_route
def create_trainer(current_user, pool_id):
    return trainer.add_trainer(current_user, pool_id)


@trainer_bp.route('/trainers/<trainer_id>/update', methods=['PUT'])
@protected_route
def update_trainer_info(current_user, trainer_id):
    return trainer.edit_trainer_info(current_user, trainer_id)

@trainer_bp.route('/trainers/<trainer_id>/delete', methods=['DELETE'])
@protected_route
def delete_trainer_info(current_user, trainer_id):
    return trainer.delete_trainer(current_user, trainer_id)


@trainer_bp.route('/trainers/<trainer_id>', methods=['GET'])
@protected_route
def get_trainer(current_user, trainer_id):
    return trainer.get_one_trainer(current_user, trainer_id)


@trainer_bp.route('/trainers', methods=['GET'])
@protected_route
def get_trainers(current_user):
    return trainer.get_trainers(current_user)


@trainer_bp.route('/trainers/pool/<pool_id>', methods=['GET'])
@protected_route
def fetch_trainers_attached_to_pool(current_user, pool_id):
    return trainer.get_trainers_attached_to_pool(current_user, pool_id)


@trainer_bp.route('/trainers/upload/<trainer_id>', methods=['POST'])
@protected_route
def upload_trainer_pic(current_user, trainer_id):
    return upload_file(current_user, trainer_id=trainer_id, table='trainer')
