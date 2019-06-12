from api.trainers import trainer_bp
from api.trainers.controllers import TrainerController
from api.auth.utilities import protected_route
from api.helpers.upload import upload_file
from api.helpers.email import send_trainer_info


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
def get_trainer(trainer_id):
    return trainer.get_one_trainer(trainer_id)


@trainer_bp.route('/trainers', methods=['GET'])
def get_trainers():
    return trainer.get_trainers()


@trainer_bp.route('/trainers/pool/<pool_id>', methods=['GET'])
def fetch_trainers_attached_to_pool(pool_id):
    return trainer.get_trainers_attached_to_pool(pool_id)


@trainer_bp.route('/trainers/upload/<trainer_id>', methods=['POST'])
@protected_route
def upload_trainer_pic(current_user, trainer_id):
    return upload_file(current_user, trainer_id=trainer_id, table='trainer')


@trainer_bp.route('/trainers/sendinfo/<trainer_id>', methods=['POST'])
@protected_route
def pool_request(current_user, trainer_id):
    return send_trainer_info(current_user, trainer_id)
