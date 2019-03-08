from flask import Flask
from instance.config import app_config
from api.auth.views import auth_bp
from api.pools import pools_bp


def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')
    # Register blueprints to the api
    app.register_blueprint(auth_bp, url_prefix='/api/v1')
    app.register_blueprint(pools_bp, url_prefix='/api/v1')
    return app
