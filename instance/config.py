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
    IMGUR_ID = "d2960a3e71db5a0"
    MAIL_SERVER = "smtp.gmail.com"
    MAIL_PORT = 465
    MAIL_USE_SSL = True
    MAIL_USERNAME = "sanyakenneth@gmail.com"
    MAIL_PASSWORD = "Hackaholic23"
    MAIL_DEFAULT_SENDER = "sanyakenneth@gmail.com"


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
    DEBUG = True
    TESTING = False
    ENV = "Production"
    SQLALCHEMY_DATABASE_URI = os.getenv('production_db')


app_config = {
    "Development": DevelopmentConfig,
    "Testing": TestingConfig,
    "Production": ProductionConfig
}
