from flask import Blueprint
from flask_cors import CORS


# setup blueprint for rate_system package
rate_bp = Blueprint('rate_bp', __name__)
# enable cors for rating system blueprint
CORS(rate_bp)