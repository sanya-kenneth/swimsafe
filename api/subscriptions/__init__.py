from flask import Blueprint
from flask_cors import CORS


# setup blueprint for subscription package
subs_bp = Blueprint('subs_bp', __name__)
# enable cors for subscription blueprint
CORS(subs_bp)