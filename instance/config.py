import os


class BaseConfig:
    """Default configuration. Details from this configuration
    class are shared across all environments  """
    DEBUG = False
    TESTING = False
    SECRET = os.getenv('SECRET')
    SQLALCHEMY_DATABASE_URI = 'postgres://postgres:psql@localhost:5432/swimsafe'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    WHOOSH_BASE = 'whoosh'
    UPLOADED_PHOTOS_DEST = 'uploads'


class DevelopmentConfig(BaseConfig):
    """Development configuraion. Loads development configuration data
    when the app is in the development environment"""
    DEBUG = True
    TESTING = False
    ENV = "Development"
    SQLALCHEMY_DATABASE_URI = 'postgres://postgres:psql@localhost:5432/swimsafe'


class TestingConfig(BaseConfig):
    """Testing configuraion. Loads Test configuration data
    when the app is in the Test environment"""
    DEBUG = True
    TESTING = True
    ENV = "Testing"
    SQLALCHEMY_DATABASE_URI = 'postgres://postgres:psql@localhost:5432/test_swimsafe'


class ProductionConfig(BaseConfig):
    """Production configuraion. Loads Production configuration data
    when the app is in the Production environment"""
    DEBUG = False
    TESTING = False
    ENV = "Production"
    SQLALCHEMY_DATABASE_URI = os.getenv('production_db')


app_config = {
    "Development": DevelopmentConfig,
    "Testing": TestingConfig,
    "Production": ProductionConfig
}