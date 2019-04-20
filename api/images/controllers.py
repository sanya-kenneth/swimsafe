from api.trainers.controllers import user_valid
from flask import jsonify
from .models import Images


def get_images_attached_to_pool(current_user, pool_id):
        """
        method returns all trainers who are attached to a given swimming
        pool
        """
        user_valid.check_user_is_loggedin(current_user)
        images_fetched = Images.query.filter_by(pool_id=pool_id).all()
        if not images_fetched:
            return jsonify({'message': 'No images found for this swimming pool',
                            'status': 404})
        image_list = []
        image_keys = ['image_id', 'image_name', 'image_url', 'pool_id']
        for single_image in images_fetched:
            image_details = [single_image.image_id, single_image.image_name,
                             single_image.image_url, single_image.pool_id]
            image_list.append(dict(zip(image_keys, image_details)))
        return jsonify({'data': image_list, 'status': 200})
