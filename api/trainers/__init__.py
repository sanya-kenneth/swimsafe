from flask import Blueprint
from flask_cors import CORS


# setup blueprint for auth package
trainer_bp = Blueprint('trainer_bp', __name__)
# enable CORS for auth blueprint
CORS(trainer_bp)