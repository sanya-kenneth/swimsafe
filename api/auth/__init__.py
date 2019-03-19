from flask import Blueprint
from flask_cors import CORS


# setup blueprint for auth package
auth_bp = Blueprint('auth_bp', __name__)
# enable CORS for auth blueprint
CORS(auth_bp)