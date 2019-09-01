# run.py

import os

from app import create_app

config_name = os.getenv('FLASK_CONFIG')

# create appropriate app object based on FLASK_CONFIG env variable
app = create_app(config_name)

if __name__ == '__main__':
    app.run()