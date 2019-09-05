# config.py

import os

# db_username = os.getenv('POSTGRES_USER')
# db_password = os.getenv('POSTGRES_PASSWORD')
# db_server = os.getenv('DB_SERVER')
# db_port = os.getenv('DB_PORT')
# db_name = os.getenv('DB_NAME')

class Config():
    # Common configurations
    #SQLALCHEMY_DATABASE_URI = f'postgres+psycopg2://{db_username}:{db_password}@{db_server}:{db_port}/{db_name}'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///simple-url'

class DevelopmentConfig(Config):
    # Development configurations
    DEBUG = True
    SQLALCHEMY_ECHO = True

class ProductionConfig(Config):
    # Production configurations
    DEBUG = False

app_config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig
}