import os

# create settings object corresponding to specified env
APP_ENV = os.environ.get("APP_ENV", "development")


class BaseConfig:
    API_PREFIX = "/api"
    TESTING = False
    DEBUG = False


class DevelopmentConfig(BaseConfig):
    FLASK_ENV = "development"
    DEBUG = True


class ProductionConfig(BaseConfig):
    FLASK_ENV = "production"


class TestingConfig(BaseConfig):
    FLASK_ENV = "development"
    TESTING = True
    DEBUG = True


config_dispatcher = {
    "development": DevelopmentConfig,
    "production": ProductionConfig,
    "testing": TestingConfig,
}

config = config_dispatcher[APP_ENV]
