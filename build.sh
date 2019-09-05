#!/bin/bash

# Create and activate virtual environment
python3 -m venv
. venv/bin/activate

# Install dependencies
pip3 install wheel  # just in case
pip3 install -r requirements.txt

# Environment Variables
export FLASK_APP=run.py
export FLASK_CONFIG=development
export POSTGRES_USER=postgres
export POSTGRES_PASSWORD=''
export DB_SERVER=localhost
export DB_PORT=5432
export DB_NAME=simple-url-test