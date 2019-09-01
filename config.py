# config.py

class DevelopmentConfig():
    # Development configurations
    DEBUG = True
    SQLALCHEMY_ECHO = True

class ProductionConfig():
    # Production configurations
    DEBUG = False

app_config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig
}