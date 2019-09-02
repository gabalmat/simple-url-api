# app/__init__.py

# third-party imports
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# local imports
from config import app_config

# db variable initialization
db = SQLAlchemy()

app = Flask(__name__, instance_relative_config=True)

# function that takes a configuration name and loads the correct configuration
def create_app(config_name):
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')

    db.init_app(app)
    migrate = Migrate(app, db)

    # load the views
    from app import views

    # load the models
    from app import models

    return app
