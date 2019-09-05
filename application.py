# run.py

import os

from app import create_app

#config_name = os.getenv('FLASK_CONFIG')
config_name = 'production'

# create appropriate app object based on FLASK_CONFIG env variable
application = create_app(config_name)

if __name__ == '__main__':
    application.run()