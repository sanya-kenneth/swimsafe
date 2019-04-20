from flask import Blueprint
from flask_cors import CORS


# setup blueprint for image package
image_bp = Blueprint('image_bp', __name__)
# enable cors for image blueprint
CORS(image_bp)