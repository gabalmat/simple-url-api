# app/api.py

from flask import jsonify, request
from sqlalchemy import exc

from app import app, db
from .models import Url, Comment
from .schemas import url_schema, urls_schema, comment_schema, comments_schema

# Add a URL
@app.route('/api/addurl', methods=['POST'])
def add_url():
    uri = request.json['uri']

    new_url = Url(uri)
    db.session.add(new_url)

    try:

        db.session.commit()
        db.session.refresh(new_url)
        return url_schema.jsonify(new_url)

    except exc.SQLAlchemyError:

        return jsonify({
            'status': 'error',
            'message': 'Record was not added due to database exception'
        })

# Get all URLs
@app.route('/api/urls/', methods=['GET'])
def get_urls():
    all_urls = Url.query.all()
    url_dict = urls_schema.dump(all_urls)

    return jsonify(url_dict)

