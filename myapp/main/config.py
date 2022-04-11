class Config(object):
    SECRET_KEY = 'e102287a92da4d6688010ac65b6a4693'
    DEBUG = False

class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///ecommerce.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = True

class ProductionConfig(Config):
    DEBUG = False

app_config = {
    'development':DevelopmentConfig,
    'production':ProductionConfig
}

