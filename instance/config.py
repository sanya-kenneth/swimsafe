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
    IMGUR_ID = "c2cf86913cc5b28"
    MAIL_SERVER = "smtp.gmail.com"
    MAIL_PORT = 465
    MAIL_USE_SSL = True
    MAIL_USERNAME = "easyswim123@gmail.com"
    MAIL_PASSWORD = "mubs2013"
    MAIL_DEFAULT_SENDER = "easyswim123@gmail.com"


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
