from flask import Blueprint
from flask_cors import CORS


# setup blueprint for pools package
pools_bp = Blueprint('pools_bp', __name__)
# enable cors for pools blueprint
CORS(pools_bp)