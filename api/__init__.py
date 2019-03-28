from flask import Flask
from instance.config import app_config
from api.auth.views import auth_bp
from api.pools.views import pools_bp
from api.trainers.views import trainer_bp
from api.subscriptions.views import subs_bp
from api.database.db import db
from flask_migrate import Migrate
from api.auth.admin import create_admin
import flask_whooshalchemyplus


def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')
    # SQLAlchemy setup with flask woosh alchemy for indexing
    app.config['SQLALCHEMY_DATABASE_URI']
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS']
    app.config['WHOOSH_BASE']
    app.config['WHOOSH_DISABLED'] = False
    db.init_app(app)
    # Setup migration engine
    migrate = Migrate(app, db)
    db.create_all(app=app)
    app_context = app.app_context()
    app_context.push()
    create_admin()
    flask_whooshalchemyplus.init_app(app)
    # Register blueprints to the api
    app.register_blueprint(auth_bp, url_prefix='/api/v1')
    app.register_blueprint(pools_bp, url_prefix='/api/v1')
    app.register_blueprint(trainer_bp, url_prefix='/api/v1')
    app.register_blueprint(subs_bp, url_prefix='/api/v1')
    return app
