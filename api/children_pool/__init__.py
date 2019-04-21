from flask import Blueprint
from flask_cors import CORS


# setup blueprint for children_pool package
children_bp = Blueprint('children_bp', __name__)
# enable cors for children_pool blueprint
CORS(children_bp)
