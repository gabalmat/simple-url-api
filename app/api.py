# app/api.py

'''
This module specifies routes and handles 
requests for all REST API endpoints
'''

from flask import jsonify, request
from sqlalchemy import exc

from app import app, db
from .models import Url, Comment
from .schemas import url_schema, urls_schema, comment_schema, comments_schema

'''
Create new URL record. Also create a new Comment record if one is provided
:param uri:  URL to be saved
:param (optional) comment: Comment to be saved when URL gets saved

:return:     Newly added URL object
'''
@app.route('/api/addurl', methods=['POST'])
def add_url():
    uri = request.json['uri']
    comment = request.json.get('comment')

    if comment:
        new_comment = Comment(comment=comment)
        new_url = Url(uri=uri, comments=[new_comment])
        db.session.add(new_comment)
    else:
        new_url = Url(uri=uri)
    
    db.session.add(new_url)

    try:
        db.session.commit()
        db.session.refresh(new_url)

        return url_schema.jsonify(new_url)
    except exc.SQLAlchemyError:
        return jsonify({
            'status': 'error',
            'message': 'URL was not added due to database exception'
        })

'''
Get all URLs and their properties

:return:  list of URLs objects
'''
@app.route('/api/urls/', methods=['GET'])
def get_urls():
    all_urls = Url.query.all()
    url_dict = urls_schema.dump(all_urls)

    return jsonify(url_dict)

'''
Get a single URL
:param url_id:  ID of URL to find

:return         URL object matching ID
'''
@app.route('/api/url/<id>', methods=['GET'])
def get_url(id):
    url = Url.query.get(id)

    if url is not None:
        return url_schema.jsonify(url)
    else:
        return jsonify({
            'status': 'error',
            'message': f'URL with id: {id} not found'
        })

'''
Create a new Comment for the given URL
:param url_id:   Integer ID of the URL to add Comment to
:param comment:  Comment to add

:return:          Newly added Comment object
'''
@app.route('/api/addcomment', methods=['POST'])
def add_comment():
    url_id = request.json['url_id']
    comment = request.json['comment']

    # Get the URL object
    url = Url.query.get(url_id)
    if url is None:
        return jsonify({
            'status': 'error',
            'message': f'URL with id: {url_id} not found'
        })

    new_comment = Comment(url=url, comment=comment)
    db.session.add(new_comment)

    try:
        db.session.commit()
        db.session.refresh(new_comment)
        return comment_schema.jsonify(new_comment)
    except exc.SQLAlchemyError:
        return jsonify({
            'status': 'error',
            'message': 'Comment was not added due to database exception'
        })