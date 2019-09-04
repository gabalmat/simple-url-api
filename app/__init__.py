# app/__init__.py

# third-party imports
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
from flask_cors import CORS

# local imports
from config import app_config

# DB variable initialization
db = SQLAlchemy()
# Marshmallow variable initialization
ma = Marshmallow()

# Initialize Flask app
app = Flask(__name__, instance_relative_config=True)
CORS(app)

'''
Load the correct configuration based on input
:param config_name: configuration name specifed in FLASK_APP env variable

:return: the Flask app object
'''
def create_app(config_name):
    app.config.from_object(app_config[config_name])

    db.init_app(app)
    ma.init_app(app)
    migrate = Migrate(app, db)

    # load the models and api
    from app import models, api

    return app
