from api.images.controllers import get_images_attached_to_pool
from api.auth.utilities import protected_route
from api.images import image_bp
from api.helpers.upload import upload_file


@image_bp.route('images/pool/<pool_id>', methods=['GET'])
@protected_route
def fetch_images_attached_to_pool(current_user, pool_id):
    return get_images_attached_to_pool(current_user, pool_id)


@image_bp.route('/images/upload/<pool_id>', methods=['POST'])
@protected_route
def upload_pool_image(current_user, pool_id):
    return upload_file(current_user, pool_id=pool_id, table='images')
